import requests
import streamlit as st
API_KEY = st.secrets["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"]

def generate_answer(context, question):

    prompt = f"""
You are a smart AI coding + study assistant.

Context:
{context}

User Question:
{question}

Instructions:

1. If the question is related to coding (Java, Python, C, program, code):
   - ALWAYS give full working code
   - Then explain the code clearly
   - Then give example input/output

2. If the question is theoretical:
   - Give clear explanation
   - Keep it simple and useful

3. Format output like ChatGPT:
   - Use emojis
   - Keep it clean and readable
   - Do NOT use headings like "Explanation", "Key Points"

4. Important:
   - NEVER skip code if question asks for code
   - Code must be complete and correct

Answer:
"""

    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "openai/gpt-4o-mini",
                "messages": [
                    {"role": "user", "content": prompt}
                ]
            }
        )

        data = response.json()

        if "choices" in data:
            return data["choices"][0]["message"]["content"]
        else:
            return f"⚠ API Error: {data}"

    except Exception as e:
        return f"⚠ Error: {str(e)}"
