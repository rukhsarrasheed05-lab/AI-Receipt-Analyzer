# AI-Receipt-Analyzer
Objective:
Build a system that extracts information from receipt images using OCR, categorizes expenses,
analyzes spending patterns, and provides personalized budgeting advice via an LLM.
Tasks / Workflow:
1. Receipt Image Processing
o Accept receipt images as input.
o Apply image preprocessing techniques such as noise reduction, grayscale
conversion, contrast enhancement, and thresholding to improve text visibility.
o Use Optical Character Recognition (OCR) techniques to extract textual
information such as item names, quantities, prices, and totals from the receipt
image.

2. Data Parsing & Structuring
o Convert OCR text into structured format (item name, price, quantity).
o Handle OCR errors and clean data.
3. Expense Categorization
o Classify each item into categories (e.g., snacks, dairy, meat, bakery).
o Calculate totals per category and overall spending.
4. Spending Analysis
o Compute percentage of total spending per category.
o Highlight overspending areas or anomalies.
5. LLM Integration for Financial Advice
o Feed structured data into a Large Language Model (LLM).
o Generate personalized insights and recommendations for budgeting.
6. Streamlit Web App Development
o Implement a user-friendly interface for uploading receipts.
o Display spending breakdown and AI-generated advice interactively.
o Visualize results with tables, charts, and textual insights from LLM.
7. Testing & Demonstration
o Test with multiple receipts to ensure accuracy.
o Prepare demo showing the full workflow: OCR → Analysis → LLM advice.

Expected Outcomes:
● Accurate extraction of items and prices from receipts.
● Automatic categorization and spending analysis.
● Clear, actionable, AI-driven financial advice.
● Fully functional working demonstration of end-to-end workflow.
