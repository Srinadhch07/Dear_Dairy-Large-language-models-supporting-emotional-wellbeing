from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from transformers import pipeline

# Load tokenizer and model
# importing models manually to setup and predict emotinons more controls and highly accurate
tokenizer = AutoTokenizer.from_pretrained("j-hartmann/emotion-english-distilroberta-base")
model = AutoModelForSequenceClassification.from_pretrained("j-hartmann/emotion-english-distilroberta-base")

# Importing predefinded model ready use model - less capable then manual one
# classifier = pipeline("text-classification", model="joeddav/distilbert-base-uncased-go-emotions-student", top_k=1)

emotions = ["admiration","amusement","anger","annoyance","approval","caring","confusion",
            "curiosity","desire","disappointment","disapproval","disgust","embarrassment",
            "excitement","fear","gratitude","grief","joy","love","nervousness","optimism",
            "pride","realization","relief","remorse","sadness","surprise","neutral"]


def predict_emotion(text):
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model(**inputs)
    probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
    max_idx = torch.argmax(probs)
    label = model.config.id2label[max_idx.item()]
    print(f"Emotion: {label}, Score: {float(probs[0][max_idx])}")
    return (label, float(probs[0][max_idx]))


# predict_emotion_correct("I'm doing greta today and I dont know why this hapened but my friend met me after long time  and we spent lot of time and did some adventures")
# result=classifier("I'm doing greta today and I dont know why this hapened but my friend met me after long time  and we spent lot of time and did some adventures")
