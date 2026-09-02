import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# 1. DATA INGESTION & AUDIT
# ==========================================
print("--- Loading Data ---")

# Using 'r' (raw string) prevents Windows backslashes from breaking the code
file_path = r"D:\prep\BA-DA\python programs\Advance-python-projects\Gurgaon real estate market analysis\data.csv"
df = pd.read_csv(file_path)

# Inspect the structure, column names, and data types
print("Dataset Shape:", df.shape)
print("\nDataset Info:")
df.info()
print("\nFirst 5 Rows:\n", df.head())

# ==========================================
# 2. DATA CLEANING & PREPARATION
# ==========================================
# Standardize column names (consistent casing, no spaces)
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Convert numeric columns from strings to integers (removes commas)
df["price"] = df["price"].astype(str).str.replace(",", "").astype(int)
df["area"] = df["area"].astype(str).str.replace(",", "").astype(int)
df["rate_per_sqft"] = df["rate_per_sqft"].astype(str).str.replace(",", "").astype(int)

# Clean categorical columns (prevents duplicate categories from formatting issues)
df["status"] = df["status"].str.strip().str.lower()
df["rera_approval"] = df["rera_approval"].str.strip().str.lower()
df["flat_type"] = df["flat_type"].str.strip().str.lower()

# Remove duplicate rows to prevent skewed averages
df = df.drop_duplicates()

# ==========================================
# 3. BUSINESS ANALYSIS
# ==========================================
print("\n--- Business Insights ---")

# Q1: Which is the costliest flat?
print("\n1. Costliest Flat:\n", df.loc[df["price"].idxmax()])

# Q2: Which locality has the highest average price?
print("\n2. Highest Avg Price by Locality:\n", 
      df.groupby("locality")["price"].mean().sort_values(ascending=False).head())

# Q3: Which locality has the highest rate per square foot? (Identifies premium locations)
print("\n3. Highest Rate per SqFt by Locality:\n", 
      df.groupby("locality")["rate_per_sqft"].mean().sort_values(ascending=False).head())

# Q4: Ready-to-move vs Under-construction pricing (Using median to ignore outliers)
print("\n4. Median Price by Status:\n", 
      df.groupby("status")["price"].median())

# Q5: Does RERA approval affect pricing? (Measures trust premium)
print("\n5. Median Price by RERA Approval:\n", 
      df.groupby("rera_approval")["price"].median())

# Q7: Which BHK configuration is most expensive? (Demand by family size)
print("\n7. Average Price by BHK Count:\n", 
      df.groupby("bhk_count")["price"].mean())

# Q8: Which property type is the costliest?
print("\n8. Average Price by Flat Type:\n", 
      df.groupby("flat_type")["price"].mean())

# Q9: Do certain builders price higher? (Brand impact)
print("\n9. Average Price by Builder:\n", 
      df.groupby("company_name")["price"].mean().sort_values(ascending=False).head())

# ==========================================
# 4. DEEPER INSIGHTS & VISUALIZATION
# ==========================================
print("\n--- Generating Visualizations ---")

# Q6: How does area impact price?
plt.figure(figsize=(10, 6))
sns.scatterplot(x="area", y="price", data=df)
plt.title("Correlation: Area vs. Price")
plt.xlabel("Area (SqFt)")
plt.ylabel("Price")
plt.show()

# Q10: Are larger homes more expensive per sqft? (Economies of scale)
plt.figure(figsize=(10, 6))
sns.scatterplot(x="area", y="rate_per_sqft", data=df)
plt.title("Economies of Scale: Area vs. Rate per SqFt")
plt.xlabel("Area (SqFt)")
plt.ylabel("Rate per SqFt")
plt.show()