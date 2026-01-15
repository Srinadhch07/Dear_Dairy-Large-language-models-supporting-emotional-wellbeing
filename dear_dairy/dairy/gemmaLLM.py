# gemmaLLM
import ollama
# from .nlp_model import predict_emotion
# from .nlp_model import classifier
import json


import json
import re

def safe_json_loads(reply_str):
    try:
        return json.loads(reply_str)
    except json.JSONDecodeError:
        # Fix common mistakes like trailing commas or missing braces
        cleaned = re.sub(r',\s*}', '}', reply_str)  # remove trailing commas
        cleaned = re.sub(r'(\{[^{}]*):\s*("[^"]*")\s*\{', r'\1: \2}, {', cleaned)  # fix missing }
        try:
            return json.loads(cleaned)
        except:
            return None


def fallback_gemma_reply(dairy_input):
    prompt = f"""
    
    You are a mental and wellbeing support AI assistant. Your job:
    1. Detect the single-word emotion from the diary text.
    2. Explain briefly why that emotion was detected.
    3. Provide a supportive and empathetic response.
    4. Provide three personalized suggestions:
        - A motivational quote
        - A self-care/relaxation tip
        - A journaling prompt

    Output your entire response strictly as a JSON object:
    {{
      "emotion": "string",
      "analysis": "string",
      "supportive_response": "string",
      "suggestions": [
        {{ "type": "quote", "text": "..." }},
        {{ "type": "self-care", "text": "..." }},
        {{ "type": "journal-prompt", "text": "..." }}
      ]
    }}
    ⚠️ IMPORTANT: Return ONLY valid JSON. Do not include explanations, text outside JSON, or missing commas/brackets.
    Now, analyze this diary entry:
    {dairy_input}
    """

    try:
        response = ollama.chat(
            model="qwen2:0.5b",
            messages=[{"role": "user", "content": prompt}],
            format="json"
        )
        reply_str = response['message']['content'].strip("` \n").lstrip("json").strip()
        return safe_json_loads(reply_str)
    except Exception as e:
        print(f"Fallback error: {e}")
        return None



def parent_supporter(text, context=""):
    prompt = f"""
You are a warm, emotionally intelligent parent companion and child-behavior guide.

Here is the recent conversation between the parent and you:
{context}

Now the parent is continuing the conversation.

You must:
- Stay supportive and friendly in every reply
- If the parent is okay, keep things warm and encouraging
- If the parent is worried, gently comfort and guide them
- Help the parent understand their child’s emotions
- Never judge, blame, or create unnecessary drama
- Speak naturally, like a kind human

Parent’s new message:
{text}

Write one natural, caring reply that continues this conversation and supports the parent.
"""

    try:
        response = ollama.chat(
            # model="qwen2:0.5b",
            model="gemma:2b",
            messages=[{"role": "user", "content": prompt}],
            options={"temperature": 0.6}
        )

        return response["message"]["content"].strip()

    except Exception as e:
        print("Parent AI error:", e)
        return "I’m here with you. It sounds like you really care about your child, and that means a lot."
