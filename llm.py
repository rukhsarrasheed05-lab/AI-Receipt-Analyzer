# llm_env.py
import os
from dotenv import load_dotenv
import pandas as pd
import openai
from dotenv import load_dotenv
import os

load_dotenv()  # Loads .env automatically
api_key = os.getenv("API_KEY")
print("Loaded API Key:", api_key[:5], "..." if api_key else "None")  # Test key load ho rahi hai ya nahi

# -----------------------------
# Load .env file
load_dotenv()  # Automatically loads variables from .env

openai.api_key = os.getenv("API_KEY")
if openai.api_key is None:
    raise ValueError("API_KEY not found in .env file!")

# -----------------------------
# Sample parsed + categorized receipt DataFrame
data = {
    "Item": ["HIX DRINK - PREMIUM", "DRAFT BEER 1602", "HOUSE WINE"],
    "Quantity": [1, 1, 2],
    "Unit Price": [6.25, 4.25, 6.25],
    "Total": [6.25, 4.25, 12.50],
    "Category": ["Drinks", "Drinks", "Drinks"]
}

df = pd.DataFrame(data)

# -----------------------------
# Convert DataFrame to summary text for LLM
def df_to_summary(df):
    summary = ""
    for _, row in df.iterrows():
        summary += f"{row['Quantity']} x {row['Item']} (${row['Total']}) - Category: {row['Category']}\n"
    summary += f"\nTotal Spending: ${df['Total'].sum()}\n"
    return summary

receipt_summary = df_to_summary(df)

# -----------------------------
# Latest OpenAI ChatCompletion (v1.0+)
prompt = f"""
You are a smart financial assistant. Based on this receipt, give personalized financial advice:
- Identify overspending categories
- Suggest ways to save money
- Highlight expensive items

Receipt data:
{receipt_summary}
"""

response = openai.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful financial assistant."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.7
)

advice = response.choices[0].message.content

print("=== LLM Financial Advice ===")
print(advice)
