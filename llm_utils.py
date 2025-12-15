import requests
import streamlit as st

OPENROUTER_API_KEY = st.secrets.get("OPENROUTER_API_KEY")

if not OPENROUTER_API_KEY:
    raise RuntimeError("OPENROUTER_API_KEY not found in Streamlit secrets")

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "openai/gpt-3.5-turbo"


def call_llm(prompt: str) -> str:
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://ai-feedback-dashboard.streamlit.app",
        "X-Title": "AI Feedback Dashboard"
    }

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.4
    }

    response = requests.post(
        OPENROUTER_URL,
        headers=headers,
        json=payload,
        timeout=30
    )

    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]


def generate_user_response(review, rating):
    prompt = f"""
You are a customer support assistant.
Write a polite response to the customer.

Rating: {rating}
Review: {review}
"""
    return call_llm(prompt)


def generate_summary(review):
    prompt = f"""
Summarize this customer feedback in one sentence:

{review}
"""
    return call_llm(prompt)


def generate_recommended_action(review, rating):
    prompt = f"""
Suggest an internal action for this feedback.

Rating: {rating}
Review: {review}
"""
    return call_llm(prompt)
