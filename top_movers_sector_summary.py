import pandas as pd
import matplotlib.pyplot as plt
import os
from db_connection import get_engine

# -----------------------------
# Create outputs folder for this script
# -----------------------------
OUTPUT_DIR = "outputs/top_movers_sector_summary"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# -----------------------------
# Connect to database
# -----------------------------
engine = get_engine()

# Fetch all data
df = pd.read_sql("SELECT * FROM stock_data", engine)
df['date'] = pd.to_datetime(df['date'])

# -----------------------------
# Define sectors
# -----------------------------
sectors = {
    "Energy & Conglomerates": ["RELIANCE.NS", "ONGC.NS"],
    "IT Services": ["TCS.NS", "INFY.NS", "WIPRO.NS"],
    "Banking & Finance": ["HDFCBANK.NS", "ICICIBANK.NS", "KOTAKBANK.NS"],
    "Automobiles": ["TATAMOTORS.NS", "MARUTI.NS"],
    "Pharma": ["SUNPHARMA.NS", "CIPLA.NS"],
    "FMCG": ["ITC.NS", "HINDUNILVR.NS"],
    "Metals": ["TATASTEEL.NS"]
}

# -----------------------------
# 1️⃣ Top & Bottom Movers by Average Daily Return
# -----------------------------
avg_returns = df.groupby('ticker')['daily_return'].mean().sort_values(ascending=False)
top5 = avg_returns.head(5)
bottom5 = avg_returns.tail(5)

# Plot top 5 movers
plt.figure(figsize=(10,5))
top5.plot(kind='bar', color='green', edgecolor='black')
plt.title("Top 5 Stocks by Average Daily Return")
plt.ylabel("Average Daily Return")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "top5_avg_daily_return.png"))
plt.show()

# Plot bottom 5 movers
plt.figure(figsize=(10,5))
bottom5.plot(kind='bar', color='red', edgecolor='black')
plt.title("Bottom 5 Stocks by Average Daily Return")
plt.ylabel("Average Daily Return")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "bottom5_avg_daily_return.png"))
plt.show()

# -----------------------------
# 2️⃣ Sector-wise Average Daily Return
# -----------------------------
sector_returns = {}
for sector, tickers in sectors.items():
    sector_returns[sector] = df[df['ticker'].isin(tickers)]['daily_return'].mean()

sector_df = pd.Series(sector_returns).sort_values(ascending=False)

plt.figure(figsize=(12,6))
sector_df.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title("Average Daily Return by Sector")
plt.ylabel("Average Daily Return")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "sector_avg_daily_return.png"))
plt.show()

# -----------------------------
# 3️⃣ Save Tables as CSV
# -----------------------------
top_bottom_csv = os.path.join(OUTPUT_DIR, "top_bottom_avg_daily_return.csv")
pd.concat([top5, bottom5], axis=0).to_csv(top_bottom_csv, header=["avg_daily_return"])
print(f"✅ Saved top & bottom movers table: {top_bottom_csv}")

sector_csv = os.path.join(OUTPUT_DIR, "sector_avg_daily_return.csv")
sector_df.to_csv(sector_csv, header=["avg_daily_return"])
print(f"✅ Saved sector summary table: {sector_csv}")
