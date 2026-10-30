
import pandas as pd
# Load the retail dataset
df = pd.read_csv("Sample - Superstore.csv", encoding="latin1")
# Display first 5 records
print("FIRST 5 RECORDS:")
print(df.head())
# Display dataset information
print("\nDATASET INFORMATION:")
print(df.info())
# Display number of rows and columns
print("\nDATASET SHAPE:")
print(df.shape)
# Check missing values
print("\nMISSING VALUES:")
print(df.isnull().sum())
