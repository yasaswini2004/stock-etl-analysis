import pandas as pd
import matplotlib.pyplot as plt
import os
from db_connection import get_engine

# -----------------------------
# Create outputs folder for this script
# -----------------------------
OUTPUT_DIR = "outputs/volatility_vs_return"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# -----------------------------
# Connect to database
# -----------------------------
engine = get_engine()

# Fetch all data
df = pd.read_sql("SELECT * FROM stock_data", engine)
df['date'] = pd.to_datetime(df['date'])

# -----------------------------
# Calculate metrics
# -----------------------------
metrics = df.groupby('ticker')['daily_return'].agg(['mean', 'std']).rename(
    columns={'mean': 'avg_daily_return', 'std': 'volatility'}
).sort_values('avg_daily_return', ascending=False)

# -----------------------------
# Scatter Plot
# -----------------------------
plt.figure(figsize=(12, 6))
plt.scatter(metrics['volatility'], metrics['avg_daily_return'], color='skyblue', edgecolor='black', s=100)

for i, ticker in enumerate(metrics.index):
    plt.text(metrics['volatility'][i], metrics['avg_daily_return'][i], ticker, fontsize=9, ha='right')

plt.title("Volatility vs Average Daily Return")
plt.xlabel("Volatility (Std of Daily Return)")
plt.ylabel("Average Daily Return")
plt.axhline(0, color='black', linestyle='--', linewidth=1)
plt.axvline(0, color='black', linestyle='--', linewidth=1)
plt.tight_layout()

scatter_file = os.path.join(OUTPUT_DIR, "volatility_vs_return.png")
plt.savefig(scatter_file)
plt.show()
print(f"✅ Saved scatter plot: {scatter_file}")

# -----------------------------
# Save metrics as CSV
# -----------------------------
csv_file = os.path.join(OUTPUT_DIR, "volatility_vs_return.csv")
metrics.to_csv(csv_file)
print(f"✅ Saved metrics table: {csv_file}")
