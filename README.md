# Dear Dairy – AI-powered Mental Wellbeing Dairy

**Tagline:** *Your AI companion for mental wellbeing and self-reflection.*

Dear Dairy is a personal journaling application built to support mental health and emotional wellbeing in young adults. It helps users log their thoughts, track moods, and receive empathetic AI-driven responses. The app is designed specifically for people struggling with **emotional suppression**, offering structured guidance, AI support, and evidence-based techniques to foster emotional expression.

*Built to address the modern challenge of unexpressed emotions and to provide a safe, private digital space for reflection.*

---

## Why We Built Dear Dairy

- Modern life often leads to **emotional suppression**, especially among young adults.
- Suppressed emotions are strongly linked to **anxiety, depression, and reduced wellbeing**.
- Journaling and expressive writing are **proven interventions** for improving mood and mental health.
- Digital solutions make journaling **accessible, private, and scalable**, allowing integration with AI for enhanced support.

---

## Features

### 🧠 Emotion Detection
- Detects user emotions using NLP models (**DistilBERT**, **Gemma:2B**, **Gemini API**).
- Can integrate HuggingFace datasets like `dair-ai/emotion` or `go_emotions`.

### 💬 AI Replies
- Generates **empathetic, supportive responses** tailored to user mood.
- Responses are dynamically generated using **Gemma / Gemini**, ensuring contextual relevance.

### 📊 Mood Insights & Trends
- Dashboard displaying **emotion and mood patterns** over time.
- Graphs for **weekly, monthly, and yearly insights**.

### 🎯 Personalized Suggestions
- Motivational quotes.
- Relaxation techniques.
- Guided journaling prompts.
- AI-powered coping strategies.

### 🎨 Interactive UI
- Modern, responsive interface using Django templates + Bootstrap + custom CSS.
- Past entries displayed as **cards** with date, text, detected emotion, and AI reply.

### 💾 Data Storage
- Stores **text, detected emotion, and AI replies** in SQLite by default.
- Scalable to MongoDB for multi-user deployments.

### 👥 Multi-user Login
- Secure registration and login.
- Each user sees only their own entries.

---

## Research-backed Approach

The application is informed by **peer-reviewed research**, highlighting:
- Emotional suppression in young adults leads to poor mental health outcomes.
- Expressive writing and journaling improve mood and reduce stress.
- Digital journaling interventions are effective and scalable.

For a detailed research summary, see [Dear Dairy Research Summary](./DEAR_DAIRY_RESEARCH.md).

---

## Technical Stack

| Layer             | Technology & Packages                       | Why Chosen                                                                 |
|------------------|--------------------------------------------|---------------------------------------------------------------------------|
| Frontend         | Django Templates + Bootstrap + CSS          | Quick, responsive UI for desktop/web; easy to style & maintain             |
| Backend          | Django + SQLite / MongoDB                   | Robust framework, ORM support, scalable storage options                   |
| AI Models        | DistilBERT, Gemma:2B (local) + Gemini API  | Accurate emotion detection & empathetic responses; local fallback for privacy |
| NLP & Embeddings | HuggingFace Transformers, tokenizers, torch | Pretrained models for emotion classification and embeddings               |
| Visualization    | Django + Charts / Graphs                    | User-friendly mood tracking over time                                     |
| Deployment       | Local / Cloud-ready (Render, Heroku, VPS)  | Flexible deployment and scalability                                        |
| Utilities & Frameworks | torch, transformers, tqdm, requests, pandas, numpy, matplotlib | Supports AI processing, data handling, and analytics                     |

---

## Installation & Setup

### Prerequisites
- Python >= 3.10
- Django >= 5.2
- SQLite (default) or MongoDB (scaling)
- **Ollama** (for local LLM hosting)
- **Gemma:2B** model

### Step 1: Install Ollama
1. Download installer from [Ollama](https://ollama.com/).
2. Install and verify:
```bash
ollama --version
```

### Step 2: Install Gemma:2B LLM
```bash
ollama pull gemma:2b
```
Ensure model is locally accessible.

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
- Ensure **Gemma:2B** is available via Ollama.
- Set **Gemini API key** in `.env` or `settings.py`.

### Step 8: Run Development Server
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000` to access the app.

---

## Future Expansion Ideas
- Mobile app frontend (React Native / Flutter).
- Community features (share entries anonymously).
- Subscription plan for premium features (extended insights, AI-driven guidance).

---

## Acknowledgements
- Built with Django, Bootstrap, **DistilBERT**, **torch**, and multiple ML frameworks.
- AI models include **Gemma:2B & Gemini API** for emotion detection and empathetic responses.
- Inspired by modern mental health practices, expressive writing research, and advanced ML techniques.

---

## Research Summary
For detailed references and peer-reviewed research supporting this project, see [Dear Dairy — Research Summary on Emotional Suppression in Young Adults](./DEAR_DAIRY_RESEARCH.md).