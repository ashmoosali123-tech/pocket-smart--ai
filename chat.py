"""LLM chat wrapper. Adjust the request format to match your provider."""
import os, requests
from dotenv import load_dotenv
from llm.prompts import SYSTEM_PROMPT, build_user_prompt

load_dotenv()

def ask(summary, question):
    key, url, model = os.getenv("LLM_API_KEY"), os.getenv("LLM_API_URL"), os.getenv("LLM_MODEL")
    if not (key and url):
        return "LLM not configured. Add LLM_API_KEY and LLM_API_URL to .env."
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": build_user_prompt(summary, question)},
        ],
    }
    try:
        r = requests.post(url, json=payload, headers={"Authorization": f"Bearer {key}"}, timeout=30)
        r.raise_for_status()
        return r.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Chat error: {e}"
