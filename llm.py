import requests
import os

# Get API key from Streamlit Secrets
API_KEY = os.getenv("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")

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
