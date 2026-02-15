# app.py
import streamlit as st
from PIL import Image
import pytesseract
import pandas as pd
import re
# OpenAI (for LLM advice)
import openai
import matplotlib.pyplot as plt

# -----------------------------
# OCR setup
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# -----------------------------
# OpenAI setup
# Replace with your OpenAI API key
openai.api_key = "x5zctWiXn473xyEPdCdBQfp62MqbjggM"

# -----------------------------
# Helper functions
def clean_text(text):
    lines = text.split("\n")
    return [line.strip() for line in lines if line.strip() != ""]

def parse_receipt(lines):
    items = []
    for line in lines:
        match = re.search(r'(\d+)\s+([A-Za-z0-9\- ]+?)\s*\$([\d\.]+)', line)
        if match:
            quantity = int(match.group(1))
            name = match.group(2).strip()
            price = float(match.group(3))
            total = quantity * price
            items.append([name, quantity, price, total])
    df = pd.DataFrame(items, columns=["Item", "Quantity", "Unit Price", "Total"])
    return df

def categorize_items(df):
    # Simple mapping; customize as needed
    category_map = {
        "HIX DRINK - PREMIUM": "Drinks",
        "DRAFT BEER 1602": "Drinks",
        "HOUSE WINE": "Drinks"
    }
    df["Category"] = df["Item"].map(category_map).fillna("Other")
    return df

def spending_analysis(df):
    overall_total = df["Total"].sum()
    category_totals = df.groupby("Category")["Total"].sum()
    category_percent = (category_totals / overall_total * 100).round(2)
    return overall_total, category_totals, category_percent

def df_to_summary(df):
    summary = ""
    for _, row in df.iterrows():
        summary += f"{row['Quantity']} x {row['Item']} (${row['Total']}) - Category: {row['Category']}\n"
    summary += f"\nTotal Spending: ${df['Total'].sum()}\n"
    return summary

def get_llm_advice(summary):
    prompt = f"""
    You are a smart financial assistant. Based on this receipt, give personalized financial advice:
    - Identify overspending categories
    - Suggest ways to save money
    - Highlight expensive items

    Receipt data:
    {summary}
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful financial assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content

# -----------------------------
# Streamlit UI
st.title("🧾 AI-Powered Receipt Analyzer")

uploaded_file = st.file_uploader("Upload a receipt image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Receipt", use_column_width=True)

    # OCR
    ocr_text = pytesseract.image_to_string(image)
    lines = clean_text(ocr_text)

    # Parse + Categorize
    df_items = parse_receipt(lines)
    df_items = categorize_items(df_items)

    if df_items.empty:
        st.warning("No items detected. Check OCR output or try another image.")
    else:
        st.subheader("📋 Parsed Receipt")
        st.dataframe(df_items)

        # Spending analysis
        overall_total, category_totals, category_percent = spending_analysis(df_items)
        st.subheader("💰 Spending per Category")
        st.dataframe(category_totals)

        st.subheader("📊 Spending Percentage per Category")
        st.bar_chart(category_percent)

        st.subheader("💵 Overall Spending")
        st.write(f"${overall_total}")

        # LLM advice
        st.subheader("🤖 AI Financial Advice")
        summary = df_to_summary(df_items)
        advice = get_llm_advice(summary)
        st.text(advice)
