# spending_analysis.py
import pandas as pd

# Sample categorized DataFrame from previous step
data = {
    "Item": ["HIX DRINK - PREMIUM", "DRAFT BEER 1602", "HOUSE WINE"],
    "Quantity": [1, 1, 2],
    "Unit Price": [6.25, 4.25, 6.25],
    "Total": [6.25, 4.25, 12.50],
    "Category": ["Drinks", "Drinks", "Drinks"]
}

df = pd.DataFrame(data)

# -----------------------------
# Total spending
overall_total = df["Total"].sum()

# Spending per category
category_totals = df.groupby("Category")["Total"].sum()

# Spending percentage per category
category_percent = (category_totals / overall_total * 100).round(2)

# Highest spending item
highest_item = df.loc[df["Total"].idxmax()]

# Overspending alert (example: category > 50% of total)
overspending_categories = category_percent[category_percent > 50]

# -----------------------------
# Output
print("=== Overall Spending ===")
print(f"${overall_total}\n")

print("=== Spending per Category ===")
print(category_totals)
print("\n=== Spending Percentage per Category ===")
print(category_percent)

print("\n=== Highest Spending Item ===")
print(highest_item[["Item", "Total", "Category"]])

if not overspending_categories.empty:
    print("\n=== Overspending Alert ===")
    for cat, perc in overspending_categories.items():
        print(f"Category '{cat}' is consuming {perc}% of total spending!")
