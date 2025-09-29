import pandas as pd

# Pick one cleaned stock to inspect
file_path = "data/cleaned/RELIANCE.NS.csv"

df = pd.read_csv(file_path)

print("✅ First 5 rows:")
print(df.head())

print("\n📊 Columns present:")
print(df.columns)

print("\n🔍 Any null values?")
print(df.isnull().sum())
