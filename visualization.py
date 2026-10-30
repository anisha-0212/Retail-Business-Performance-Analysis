import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load cleaned dataset
df = pd.read_csv("cleaned_superstore.csv")
# Set chart style
sns.set_theme(style="whitegrid")
# CHART 1: Profit by Product Category
category_profit = df.groupby("Category")["Profit"].sum()
plt.figure(figsize=(8, 5))
category_profit.plot(kind="bar")
plt.title("Profit by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Profit")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("profit_by_category.png")
plt.show()
plt.close()
# CHART 2: Sales by Region
region_sales = df.groupby("Region")["Sales"].sum()
plt.figure(figsize=(8, 5))
region_sales.plot(kind="bar")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("sales_by_region.png")
plt.show()
plt.close()
# CHART 3: Profit by Sub-Category
subcategory_profit = df.groupby("Sub-Category")["Profit"].sum().sort_values()
plt.figure(figsize=(10, 6))
subcategory_profit.plot(kind="bar")
plt.title("Profit by Sub-Category")
plt.xlabel("Product Sub-Category")
plt.ylabel("Total Profit")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("profit_by_subcategory.png")
plt.show()
plt.close()
print("All three charts created successfully!")
