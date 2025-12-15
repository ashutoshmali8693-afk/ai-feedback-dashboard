import requests


OPENROUTER_API_KEY = "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"


def call_llm(prompt: str) -> str:
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",
        "X-Title": "Fynd Take Home Task"
    }

    payload = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3
    }

    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"]


def generate_user_response(review, rating):
    prompt = f"""
You are a customer support assistant.
Respond politely and empathetically.

Rating: {rating}
Review: "{review}"
"""
    return call_llm(prompt)


def generate_summary(review):
    prompt = f"""
Summarize this customer review in one short sentence.

Review: "{review}"
"""
    return call_llm(prompt)


def generate_recommended_action(review, rating):
    prompt = f"""
Based on the review and rating, suggest one internal action.

Rating: {rating}
Review: "{review}"
"""
    return call_llm(prompt)
