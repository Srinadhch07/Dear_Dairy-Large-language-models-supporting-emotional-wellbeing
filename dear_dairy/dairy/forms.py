from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    role = forms.ChoiceField(
        choices=User.ROLE_CHOICES,
        initial="child",
        widget=forms.Select(attrs={
            "style": """
                width:100%;
                padding:12px 15px;
                margin:12px 0;
                border:1px solid #d1d5db;
                border-radius:8px;
                font-size:15px;
                background: rgba(255,255,255,0.95);
                color:#111827;
                appearance:none;
                cursor:pointer;
                transition:0.3s ease;
            """
        })
    )


    class Meta:
        model = User
        fields = ("username", "email", "role", "password1", "password2")
