# Dear Dairy – AI-powered Mental Wellbeing Dairy

**Tagline:** *Your AI companion for mental wellbeing and self-reflection.*

Dear Dairy is a personal journaling application designed to support mental health and emotional wellbeing. Users can log their thoughts, track moods, and receive empathetic AI-driven responses. Utilizing large language models like **Gemma:2B** and the **Gemini API**, the app generates supportive replies and provides insights on emotional trends.

*Baked by focusing on untold thoughts and emotional entanglements*

---

## Features

### 🧠 Emotion Detection
- Detects user emotions using NLP models (**Gemma:2B**, **Gemini API**).
- Optionally integrate **HuggingFace datasets** like `dair-ai/emotion` or `go_emotions`.

### 💬 AI Replies
- Generates **empathetic, supportive responses** tailored to user mood.
- Responses are dynamically generated; no fixed replies.
- Uses **Gemma / Gemini** for natural language responses.

### 📊 Mood Insights & Trends
- Dashboard displaying **mood patterns over time**.
- Graphs for emotions **weekly, monthly, yearly**.

### 🎯 Personalized Suggestions
- Motivational quotes.
- Relaxation techniques.
- Journaling prompts.
- AI-generated coping strategies.

### 🎨 Interactive UI
- Home page with attractive CSS (cards, Bootstrap themes, gradients).
- Past entries displayed as **cards** with date, text, emotion, and AI reply.

### 💾 Storage
- Saves **text, detected emotion, and AI reply** into **SQLite** (or **MongoDB** for scaling).

### 👥 Multi-user Login
- Users can register and log in securely.
- Each user sees only their own entries.

---

## Technical Stack
- **Frontend:** Django templates + Bootstrap + custom CSS
- **Backend:** Django + SQLite (later MongoDB)
- **AI Models:** Gemma:2B (local) + Gemini API (fallback support)
- **Visualization:** Dashboards for mood patterns

---

## Installation & Setup

### Prerequisites
- Python >= 3.10
- Django >= 4.0
- SQLite (default) or MongoDB (for scaling)
- **Ollama** (for local LLM hosting)
- **Gemma:2B** model

### Step 1: Install Ollama
1. Visit [Ollama website](https://ollama.com/) and download the installer for your OS.
2. Install Ollama locally following instructions.
3. Verify installation:
```bash
ollama --version
```

### Step 2: Install Gemma:2B LLM
1. Open terminal and pull Gemma:2B via Ollama:
```bash
ollama pull gemma:2b
```
2. Ensure the model is downloaded and accessible locally.

### Step 3: Clone Repository
```bash
git clone https://github.com/Srinadhch07/Dear-Dairy-Large-language-models-supporting-emotional-wellbeing.git
cd Dear-Dairy-Large-language-models-supporting-emotional-wellbeing
```

### Step 4: Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

### Step 5: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 6: Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 7: Configure AI Access
- Ensure **Gemma:2B** is available through Ollama.
- Set **Gemini API key** in `.env` or `settings.py`.

### Step 8: Run Development Server
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000` to access the app.

---

## Future Expansion Ideas
- Mobile app (React Native / Flutter frontend).
- Community feature (share Dairy entries anonymously).
- Subscription plan for premium features (deep insights, longer storage, AI-powered advice).

---

## Acknowledgements
- Built with Django, Bootstrap, and LLMs (Gemma:2B & Gemini API).
- Inspired by modern mental health and journaling practices.

