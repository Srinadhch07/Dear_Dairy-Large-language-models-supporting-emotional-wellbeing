from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.db.models import Count
from django.db.models.functions import TruncDate, TruncWeek, TruncMonth
import json
from django.core.serializers.json import DjangoJSONEncoder

from .forms import CustomUserCreationForm

from django.shortcuts import render, redirect
from .models import DiaryEntry, ParentChat

#  LLM's AI and ML models
from .gemini import generate_gemma_replay
from .gemmaLLM import fallback_gemma_reply, parent_supporter




# from .nlp_model import predict_emotion
# from .nlp_model import classifier

# from .phi3_reply import generate_phi3_reply
# from .tinyllama_reply import generate_tinyllama_reply




def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

@login_required
def role_redirect(request):
    user = request.user

    if user.role == "child":
        return redirect("home")   # diary home
    elif user.role == "parent":
        return redirect("parent_dashboard")  # we will create this
    else:
        return redirect("login")


@login_required
def home_view(request):
    
    try:
        entries = DiaryEntry.objects.filter(user=request.user).order_by('-created_at')
        return render(request, 'dairy/home.html', {'entries': entries})
    except Http404:
        return render(request, 'dairy/404.html', status=404)

@login_required 
@login_required
def index(request):
    if request.method == "POST":
        try:
            text = request.POST.get("text", "").strip()

            if not text:
                return render(request, "dairy/index.html", {
                    "error": "Please write something."
                })

            # Try Gemini first
            ai_reply_dict, ai_emotion = generate_gemma_replay(text)

            # If Gemini fails → fallback to local LLM
            if not ai_reply_dict:
                print("Primary AI failed, falling back to Gemma...")
                ai_reply_dict = fallback_gemma_reply(text)
                ai_emotion = ai_reply_dict.get("emotion", "unknown").lower()

            if not ai_reply_dict:
                return render(request, "dairy/index.html", {
                    "error": "AI could not respond. Please try again."
                })

            # Save diary
            DiaryEntry.objects.create(
                user=request.user,
                text=text,
                detected_emotion=ai_emotion,
                emotion_analysis=ai_reply_dict.get("analysis", ""),
                supportive_reply=ai_reply_dict.get("supportive_response", ""),
                suggestions=json.dumps(ai_reply_dict.get("suggestions", []))
            )

            return render(request, "dairy/suggestion.html", {
                "supportive_reply": ai_reply_dict.get("supportive_response", ""),
                "suggestions": ai_reply_dict.get("suggestions", [])
            })

        except Exception as e:
            print("Index error:", e)
            return render(request, "dairy/index.html", {
                "error": "Something went wrong. Please try again."
            })

    return render(request, "dairy/index.html")

def view_entries(request):
    
    try:
        entries = DiaryEntry.objects.filter(user=request.user).order_by('-created_at')
        return render(request, 'dairy/entries.html', {'entries': entries})
    except Http404:
        return render(request, 'dairy/404.html', status=404)
    
def entry_detail(request, pk):

    try:
        entry = get_object_or_404(DiaryEntry, pk=pk, user=request.user)
        # raise Http404("Testing custom 404 page")
        return render(request, 'dairy/entry_detail.html', {'entry': entry})
    except Http404:
        return render(request, 'dairy/404.html', status=404)
    
def delete_entry(request,pk):
    try:
        entry = DiaryEntry.objects.get(pk=pk, user=request.user)
        entry.delete()
    except DiaryEntry.DoesNotExist:
        pass
    return redirect('view_entries')

def mood_dashboard(request):
    filter_type = request.GET.get('filter', 'daily')

    if filter_type == 'weekly':
        trunc = TruncWeek('created_at')
    elif filter_type == 'monthly':
        trunc = TruncMonth('created_at')
    else:
        trunc = TruncDate('created_at') 

    data = (DiaryEntry.objects
            .filter(user=request.user)
            .annotate(period=trunc)
            .values('period', 'detected_emotion')
            .annotate(count=Count('id'))
            .order_by('period'))
    
    
    chart_data = json.dumps(list(data), cls=DjangoJSONEncoder)

    return render(request, 'dairy/dashboard.html', {
        'chart_data': chart_data,
        'filter_type': filter_type
    })

# Parent views

@login_required
def parent_dashboard(request):
    if request.user.role != "parent":
        return redirect("home")

    return render(request, "parent/dashboard.html", {
        "username": request.user.username
    })

@login_required
def parent_chat(request):
    if request.user.role != "parent":
        return redirect("home")

    chats = ParentChat.objects.filter(parent=request.user).order_by("created_at")

    if request.method == "POST":
        text = request.POST.get("text", "").strip()

        if text:
            # Get last 5 messages for context
            last_chats = ParentChat.objects.filter(parent=request.user).order_by("-created_at")[:2]

            context = ""
            for chat in reversed(last_chats):
                context += f"Parent: {chat.message}\nAI: {chat.ai_reply}\n"


            ai_reply = parent_supporter(text, context)

            ParentChat.objects.create(
                parent=request.user,
                message=text,
                ai_reply=ai_reply
            )

        return redirect("parent_chat")

    return render(request, "parent/chat.html", {"chats": chats})


@login_required
def delete_parent_chats(request):
    if request.user.role != "parent":
        return redirect("home")

    ParentChat.objects.filter(parent=request.user).delete()
    return redirect("parent_chat")
