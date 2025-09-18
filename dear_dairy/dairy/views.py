from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.db.models import Count
from django.db.models.functions import TruncDate, TruncWeek, TruncMonth
import json
from django.core.serializers.json import DjangoJSONEncoder


from django.shortcuts import render, redirect
from .models import DiaryEntry

#  LLM's AI and ML models
from .gemini import generate_gemma_replay
from .gemmaLLM import fallback_gemma_reply




from .nlp_model import predict_emotion
# from .nlp_model import classifier

# from .phi3_reply import generate_phi3_reply
# from .tinyllama_reply import generate_tinyllama_reply


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def home_view(request):
    
    try:
        entries = DiaryEntry.objects.filter(user=request.user).order_by('-created_at')
        return render(request, 'dairy/home.html', {'entries': entries})
    except Http404:
        return render(request, 'dairy/404.html', status=404)

@login_required 
def index(request):
    try:
        if request.method == "POST":
            text = request.POST.get("text")
            # Fetching emotions from disitlroberta-base model
            emotion,score = predict_emotion(text)
            
            # Fetching reply from API (preferred)
            ai_reply_dict,ai_emotion = generate_gemma_replay(text)
            if not ai_reply_dict:
                print("Primary AI failed, falling back to Gemma...")
                # Fetching reply from LLM (secondary preference)
                ai_reply_dict = fallback_gemma_reply(text)
                if ai_reply_dict:
                    ai_emotion = ai_reply_dict.get("emotion", "unknown").lower()


            if ai_reply_dict and ai_emotion:
                if ai_reply_dict and ai_emotion:
                    DiaryEntry.objects.create(
                        user=request.user,
                        text=text, 
                        detected_emotion=emotion,  # We can swtich emotion - from AI, LLM, ML model
                        emotion_analysis=ai_reply_dict.get('analysis', ''),
                        supportive_reply=ai_reply_dict.get('supportive_response', ''),
                        # Use json.dumps() to store the suggestions list as a string
                        suggestions=json.dumps(ai_reply_dict.get('suggestions', []))
                    )
                supportive_reply=ai_reply_dict.get('supportive_response', '')
                suggestions = ai_reply_dict.get('suggestions', [])
                return render(request, 'dairy/suggestion.html', {'suggestions': suggestions, 'supportive_reply':supportive_reply})

            else:
                print("Failed to get a valid response from AI.")
                return render(request, 'dairy/index.html', {'error': 'Failed to get AI response. Please try again.'})  
        return render(request, 'dairy/index.html')
    except:
        return render(request, 'dairy/404.html', status=404)

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
