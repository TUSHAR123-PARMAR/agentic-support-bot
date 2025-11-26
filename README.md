# Agentic AI Support Bot

A small agentic AI system that answers user questions using:
- FAQ-based retrieval with TF–IDF similarity
- An LLM (OpenAI) to generate final support answers

## Features

- Streamlit web interface
- Searches a local FAQ knowledge base
- Shows similarity scores and matched FAQs
- Uses LLM with context for accurate responses
- Fallback behaviour when FAQ does not contain the answer

## Tech Stack

- Python
- Streamlit
- Scikit-learn (TF–IDF + cosine similarity)
- OpenAI LLM API

## Screenshots

## 📸 Screenshots

### 1️⃣ Password Reset Question
![Reset Password 1](https://github.com/TUSHAR123-PARMAR/agentic-support-bot/blob/main/assets/screenshots/01_reset_password.jpg)
![Reset Password 2](https://github.com/TUSHAR123-PARMAR/agentic-support-bot/blob/main/assets/screenshots/02_reset_password.jpg)

---

### 2️⃣ Agentic AI Explanation
![Agentic AI 1](https://github.com/TUSHAR123-PARMAR/agentic-support-bot/blob/main/assets/screenshots/03_agentic_ai.jpg)
![Agentic AI 2](https://github.com/TUSHAR123-PARMAR/agentic-support-bot/blob/main/assets/screenshots/04_agentic_ai.jpg)

---

### 3️⃣ Out-of-FAQ Handling (Example – UPI Payments)
![Out of FAQ 1](https://github.com/TUSHAR123-PARMAR/agentic-support-bot/blob/main/assets/screenshots/05_out_of_faq.jpg)
![Out of FAQ 2](https://github.com/TUSHAR123-PARMAR/agentic-support-bot/blob/main/assets/screenshots/06_out_of_faq.jpg)


## Run locally

```bash
git clone https://github.com/TUSHAR123-PARMAR/agentic-support-bot.git
cd agentic-support-bot
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py


