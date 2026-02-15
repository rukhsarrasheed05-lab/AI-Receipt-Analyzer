# categorize.py
import pandas as pd

# Sample parsed DataFrame from parser.py
data = {
    "Item": ["HIX DRINK - PREMIUM", "DRAFT BEER 1602", "HOUSE WINE"],
    "Quantity": [1, 1, 2],
    "Unit Price": [6.25, 4.25, 6.25],
    "Total": [6.25, 4.25, 12.50]
}

df_items = pd.DataFrame(data)

# -----------------------------
# Step 1: Define category mapping
category_map = {
    "HIX DRINK - PREMIUM": "Drinks",
    "DRAFT BEER 1602": "Drinks",
    "HOUSE WINE": "Drinks"
    # Agar aur items ho to yahan add karo
}

# Step 2: Assign categories
df_items["Category"] = df_items["Item"].map(category_map).fillna("Other")

# Step 3: Calculate totals per category
category_totals = df_items.groupby("Category")["Total"].sum()

# Step 4: Calculate overall total
overall_total = df_items["Total"].sum()

# -----------------------------
# Step 5: Print results
print("=== Categorized Receipt ===")
print(df_items)

print("\n=== Spending per Category ===")
print(category_totals)

print("\n=== Overall Spending ===")
print(overall_total)
