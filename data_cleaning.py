import pandas as pd
# Load dataset
df = pd.read_csv("Sample - Superstore.csv", encoding="latin1")
# Convert date columns into datetime format
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])
# Remove duplicate records
df = df.drop_duplicates()
# Create year and month columns
df["Order Year"] = df["Order Date"].dt.year
df["Order Month"] = df["Order Date"].dt.month_name()
# Calculate profit margin
df["Profit Margin"] = (df["Profit"] / df["Sales"]) * 100
# Save cleaned dataset
df.to_csv("cleaned_superstore.csv", index=False)
print("DATA CLEANING COMPLETED!")
print("Total records:", len(df))
print("\nCleaned dataset:")
print(df.head())
print("\nCleaned dataset saved successfully!")
