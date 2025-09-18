
import google.generativeai as genai
import os
from dotenv import load_dotenv
import json
load_dotenv()


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[])
def generate_gemma_replay(dairy_input):
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
        convo.send_message(prompt)
        ai_reply_string = convo.last.text

        cleaned_string = ai_reply_string.strip('` \n').lstrip('json').strip()

        ai_reply_dict = json.loads(cleaned_string)

        emotion = ai_reply_dict.get('emotion', 'unknown').lower()

        return ai_reply_dict, emotion
    
      except Exception as e:
        print(f"An error occurred: {e}")

        return None, None 



