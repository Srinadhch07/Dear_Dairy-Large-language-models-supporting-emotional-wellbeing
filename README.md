# Dear Diary – AI-powered Mental Wellbeing Diary for Teenagers & Parents

**Tagline:** *A shared path to understanding emotions—bridging teenagers and parents.*

Dear Diary is an AI-powered journaling and emotional wellbeing platform designed to support **teenagers** and help **parents better understand their emotional world**.

It provides a safe, private space where teenagers can freely express their thoughts, track moods, and receive empathetic AI-driven responses—while promoting emotional awareness, trust, and healthier communication within families.

The platform focuses on a critical adolescent challenge: **emotional suppression, misunderstood feelings, and the widening emotional gap between teenagers and parents**.

*Built to support emotional expression during formative years and to foster empathy, emotional literacy, and resilience.*

---

## Why We Built Dear Diary

* Teenagers often struggle to **express emotions openly** to parents or guardians.
* Emotional suppression during adolescence is strongly linked to:

  * Anxiety
  * Stress
  * Burnout
  * Low self-esteem
* Parents want to help but often **don’t know what their teenager is feeling internally**.
* Journaling and expressive writing are **proven psychological tools** for emotional regulation.
* AI enables **non-judgmental, always-available emotional support**.

---

## Research Foundation

Dear Diary is grounded in well-established psychological and behavioral research:

### Emotional Suppression in Teenagers

* Adolescents often suppress emotions due to fear of judgment, academic pressure, and social expectations.
* Long-term suppression increases risk of anxiety, emotional dysregulation, and mental health challenges.

### Expressive Writing & Journaling

* Expressive writing improves emotional clarity and self-awareness.
* Regular journaling reduces stress and supports emotional regulation.

### Digital Mental Health Interventions

* Digital tools increase consistency and accessibility.
* Privacy-first journaling encourages honesty and emotional openness.
* AI-driven feedback increases engagement and emotional validation.

---

## Features

### 🧠 Emotion Detection

* Automatically detects emotional tone from journal entries.
* Uses NLP models including:

  * **DistilBERT**
  * **qwen2:0.5b**
  * **Gemini API**
* Supports emotion datasets such as:

  * `dair-ai/emotion`
  * `go_emotions`

### 💬 AI Emotional Support

* Generates empathetic, age-appropriate responses.
* Encourages emotional expression instead of suppression.
* Uses **Gemma / Gemini** for context-aware replies.

### 📊 Mood Insights & Trends

* Visual dashboards showing:

  * Daily mood patterns
  * Weekly and monthly emotional trends
* Helps teenagers identify emotional cycles.
* Supports parent understanding with consent (no private text exposure).

### 🎯 Personalized Suggestions

* Guided journaling prompts
* Emotional regulation exercises
* Relaxation and grounding techniques
* Motivational and supportive messages

### 🎨 Teen-friendly UI

* Clean, modern interface built with:

  * Django Templates
  * Bootstrap
  * Custom CSS
* Journal entries displayed as cards showing date, emotion, and AI response.

### 💾 Secure Data Storage

* Stores journal text, detected emotions, and AI responses.
* SQLite by default.
* MongoDB supported for scalable deployments.

### 👥 Multi-user Support

* Secure authentication system.
* Each teenager has a private account.
* Privacy-first and ethics-focused design.

---

## Technical Stack

| Layer         | Technology                         | Purpose                        |
| ------------- | ---------------------------------- | ------------------------------ |
| Frontend      | Django Templates, Bootstrap, CSS   | Responsive UI                  |
| Backend       | Django                             | Secure application logic       |
| Database      | SQLite / MongoDB                   | Data storage                   |
| AI Models     | DistilBERT, qwen2:0.5b, Gemini API | Emotion detection & AI replies |
| NLP           | HuggingFace Transformers, torch    | Text understanding             |
| Visualization | Charts & Graphs                    | Mood tracking                  |
| Deployment    | Local / Render / VPS               | Flexible hosting               |

---

## Installation & Execution Steps

### Prerequisites

* Python **3.10 or higher**
* Django **5.2 or higher**
* SQLite (default) or MongoDB
* **Ollama** (for running local LLMs)

---

### Step 1: Install Ollama

Download and install Ollama from:
[https://ollama.com](https://ollama.com)

Verify installation:

```bash
ollama --version
```

---

### Step 2: Download Required AI Models

```bash
ollama pull qwen2:0.5b
ollama pull gemma:2b
```

Ensure both models are available locally.

---

### Step 3: Clone the Repository

```bash
git clone https://github.com/Srinadhch07/Dear-Dairy-Large-language-models-supporting-emotional-wellbeing.git
cd Dear-Dairy-Large-language-models-supporting-emotional-wellbeing
```

---

### Step 4: Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```

---

### Step 5: Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

### Step 6: Run Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### Step 7: Configure AI Access

* Ensure **qwen2:0.5b** is accessible via Ollama
* Add your **Gemini API key** to `.env` or `settings.py`

Example:

```env
GEMINI_API_KEY=your_api_key_here
```

---

### Step 8: Run the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

```
http://127.0.0.1:8000
```

---

## Usage Flow

1. Register or log in as a user.
2. Write a daily journal entry.
3. The system detects emotional tone automatically.
4. AI generates an empathetic response.
5. Mood insights are updated on the dashboard.

---

## Future Expansion Ideas

* Parent–teen emotional insight dashboard (consent-based)
* Mobile app (React Native / Flutter)
* School counseling integrations
* Emotional literacy learning modules
* Crisis escalation support

---

## Acknowledgements

* Built using **Django**, **Bootstrap**, **DistilBERT**, and **PyTorch**
* AI powered by **qwen2:0.5b** and **Gemini**
* Inspired by adolescent psychology, expressive writing research, and digital mental health practices

---

## License

This project is intended for **educational, research, and mental wellbeing purposes**, with a focus on **teenage emotional health and parent–te
