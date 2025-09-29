import pandas as pd
import matplotlib.pyplot as plt
import os
from db_connection import get_engine

# -----------------------------
# Create outputs folder for this script
# -----------------------------
OUTPUT_DIR = "outputs/return_vs_volatility"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# -----------------------------
# Connect to database
# -----------------------------
engine = get_engine()

# Fetch all data
df = pd.read_sql("SELECT * FROM stock_data", engine)
df['date'] = pd.to_datetime(df['date'])

# -----------------------------
# Compute 20-day rolling volatility
# -----------------------------
volatility = df.pivot(index='date', columns='ticker', values='daily_return').rolling(window=20).std()

# Compute average daily return for each stock
avg_returns = df.groupby('ticker')['daily_return'].mean()

# Compute average volatility for each stock
avg_volatility = volatility.mean()

# -----------------------------
# Plot Return vs Volatility
# -----------------------------
plt.figure(figsize=(12,8))
for ticker in avg_returns.index:
    plt.scatter(avg_volatility[ticker], avg_returns[ticker], label=ticker, s=100)

plt.xlabel("Average 20-Day Rolling Volatility")
plt.ylabel("Average Daily Return")
plt.title("Return vs Volatility per Stock")
plt.grid(True)
plt.legend()
plt.tight_layout()

# Save plot
output_file = os.path.join(OUTPUT_DIR, "return_vs_volatility.png")
plt.savefig(output_file)
plt.show()
print(f"✅ Saved scatter plot: {output_file}")

# -----------------------------
# Save table as CSV
# -----------------------------
summary_df = pd.DataFrame({
    "avg_daily_return": avg_returns,
    "avg_volatility": avg_volatility
})
summary_csv = os.path.join(OUTPUT_DIR, "return_vs_volatility.csv")
summary_df.to_csv(summary_csv)
print(f"✅ Saved summary table: {summary_csv}")
