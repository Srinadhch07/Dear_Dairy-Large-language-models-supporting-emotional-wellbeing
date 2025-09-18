from django.db import models
from django.contrib.auth.models import User

class DiaryEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    detected_emotion = models.CharField(max_length=50)
    emotion_analysis = models.TextField()
    supportive_reply = models.TextField()
    suggestions = models.TextField() 
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.created_at}: {self.detected_emotion}"
