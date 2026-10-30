import pandas as pd
# Load cleaned dataset
df = pd.read_csv("cleaned_superstore.csv")
# Overall business performance
print("OVERALL BUSINESS PERFORMANCE")
print("Total Sales:", round(df["Sales"].sum(), 2))
print("Total Profit:", round(df["Profit"].sum(), 2))
print("Total Quantity Sold:", df["Quantity"].sum())
# Profit by category
print("\nPROFIT BY CATEGORY")
print(df.groupby("Category")["Profit"].sum().sort_values(ascending=False))
# Sales by region
print("\nSALES BY REGION")
print(df.groupby("Region")["Sales"].sum().sort_values(ascending=False))
# Profit by sub-category
print("\nPROFIT BY SUB-CATEGORY")
print(df.groupby("Sub-Category")["Profit"].sum().sort_values())
# Discount and profit analysis
print("\nAVERAGE PROFIT BY DISCOUNT")
print(df.groupby("Discount")["Profit"].mean().round(2))

