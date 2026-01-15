from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    ROLE_CHOICES = [
        ("child", "Child"),
        ("parent", "Parent"),
    ]

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default="child"
    )


class DiaryEntry(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    text = models.TextField()
    detected_emotion = models.CharField(max_length=50)
    emotion_analysis = models.TextField()
    supportive_reply = models.TextField()
    suggestions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.created_at}: {self.detected_emotion}"
    
class ParentChat(models.Model):
    parent = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    ai_reply = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.parent.username} - {self.created_at}"

