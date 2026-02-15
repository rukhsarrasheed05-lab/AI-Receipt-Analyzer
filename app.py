# groq_llm.py

import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

api_key = os.getenv("API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env file")

client = Groq(api_key=api_key)

# Example prompt (you can replace with receipt summary)
prompt = """
You are a smart financial assistant.
Give budgeting advice for someone who spent most of their money on drinks.
"""

completion = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0.6,
    max_completion_tokens=1024,
    top_p=0.95,
    stream=True
)

print("=== AI Financial Advice ===\n")

for chunk in completion:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="")
