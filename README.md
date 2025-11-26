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

### 1. Password reset question
![Reset Password]([assets/screenshots/01_reset_password.png](https://github.com/TUSHAR123-PARMAR/agentic-support-bot/blob/main/assets/screenshots/01_reset_password.png.jpg))

### 2. Agentic AI explanation
![Agentic AI](assets/screenshots/02_agentic_ai.png)

### 3. Out-of-FAQ question (UPI payments)
![Out of FAQ](assets/screenshots/03_out_of_faq.png)

## Run locally

```bash
git clone https://github.com/TUSHAR123-PARMAR/agentic-support-bot.git
cd agentic-support-bot
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py


