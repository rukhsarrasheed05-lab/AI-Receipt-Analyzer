# parser.py
import re
import pandas as pd

def clean_text(text):
    """
    OCR text ko clean karo:
    - Empty lines remove karo
    - Extra spaces remove karo
    """
    lines = text.split("\n")
    lines = [line.strip() for line in lines if line.strip() != ""]
    return lines

def parse_receipt(lines):
    """
    OCR text lines ko structured DataFrame me convert karo
    Format: Item, Quantity, Unit Price, Total
    Flexible regex: handles lines like:
    "1 HIX DRINK - PREMIUM $6.25"
    "2 HOUSE WINE $6.25"
    """
    items = []

    for line in lines:
        # Regex: quantity first, item name, then $price
        match = re.search(r'(\d+)\s+([A-Za-z0-9\- ]+?)\s*\$([\d\.]+)', line)
        if match:
            quantity = int(match.group(1))
            name = match.group(2).strip()
            price = float(match.group(3))
            total = quantity * price
            items.append([name, quantity, price, total])
        else:
            # OCR errors ya non-item lines ignore karo
            continue

    df = pd.DataFrame(items, columns=["Item", "Quantity", "Unit Price", "Total"])
    return df

# -------------------------------
# Test code
if __name__ == "__main__":
    sample_text = """
1 HIX DRINK - PREMIUM $6.25
1 DRAFT BEER 1602 $4.25
2 HOUSE WINE $6.25
CASH
SUB-TOTAL: $10.75
TAX $7.00
TOTAL $25.75
"""
    lines = clean_text(sample_text)
    df = parse_receipt(lines)

    print("=== Parsed Receipt ===")
    print(df)
