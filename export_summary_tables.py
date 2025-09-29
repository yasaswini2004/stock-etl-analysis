# export_summary_tables.py
import pandas as pd
import os
from db_connection import get_engine

# -----------------------------
# Create outputs folder for this script
# -----------------------------
OUTPUT_DIR = "outputs/export_summary_tables"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# -----------------------------
# Connect to database
# -----------------------------
engine = get_engine()

# Fetch all stock data
df = pd.read_sql("SELECT * FROM stock_data", engine)
df['date'] = pd.to_datetime(df['date'])

# -----------------------------
# 1️⃣ Summary: Average Daily Returns per Stock
# -----------------------------
avg_returns = df.groupby('ticker')['daily_return'].mean().sort_values(ascending=False)
avg_returns_file = os.path.join(OUTPUT_DIR, "avg_daily_return_per_stock.csv")
avg_returns.to_csv(avg_returns_file, header=["avg_daily_return"])
print(f"✅ Saved: {avg_returns_file}")

# -----------------------------
# 2️⃣ Summary: Volatility (Std Dev of Daily Returns) per Stock
# -----------------------------
volatility = df.groupby('ticker')['daily_return'].std().sort_values(ascending=False)
volatility_file = os.path.join(OUTPUT_DIR, "volatility_per_stock.csv")
volatility.to_csv(volatility_file, header=["volatility"])
print(f"✅ Saved: {volatility_file}")

# -----------------------------
# 3️⃣ Summary: Average Daily Returns per Sector
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

sector_avg_returns = {}
for sector, tickers in sectors.items():
    sector_avg_returns[sector] = df[df['ticker'].isin(tickers)]['daily_return'].mean()

sector_avg_returns = pd.Series(sector_avg_returns).sort_values(ascending=False)
sector_avg_file = os.path.join(OUTPUT_DIR, "avg_daily_return_per_sector.csv")
sector_avg_returns.to_csv(sector_avg_file, header=["avg_daily_return"])
print(f"✅ Saved: {sector_avg_file}")

# -----------------------------
# 4️⃣ Summary: 20-Day Rolling Volatility per Stock
# -----------------------------
rolling_vol = df.pivot(index='date', columns='ticker', values='daily_return').rolling(20).std()
rolling_vol_file = os.path.join(OUTPUT_DIR, "rolling_volatility_20days.csv")
rolling_vol.to_csv(rolling_vol_file)
print(f"✅ Saved: {rolling_vol_file}")
