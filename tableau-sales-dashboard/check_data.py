import csv

file = "data/sales.csv"

with open(file, newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

sales = sum(float(row["Sales"]) for row in rows)
profit = sum(float(row["Profit"]) for row in rows)
quantity = sum(int(row["Quantity"]) for row in rows)

print("===== SALES DATA SUMMARY =====")
print(f"Records : {len(rows)}")
print(f"Sales   : ₹{sales:,.2f}")
print(f"Profit  : ₹{profit:,.2f}")
print(f"Quantity: {quantity:,}")
print(f"Margin  : {(profit / sales) * 100:.2f}%")
