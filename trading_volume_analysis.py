import pandas as pd
import matplotlib.pyplot as plt
import os
from db_connection import get_engine

# Create outputs folder for this analysis
OUTPUT_DIR = os.path.join("outputs", "trading_volume_analysis")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Connect to database
engine = get_engine()

# Fetch all data
df = pd.read_sql("SELECT * FROM stock_data", engine)
df['date'] = pd.to_datetime(df['date'])

# Define sectors and stocks
sectors = {
    "Energy & Conglomerates": ["RELIANCE.NS", "ONGC.NS"],
    "IT Services": ["TCS.NS", "INFY.NS", "WIPRO.NS"],
    "Banking & Finance": ["HDFCBANK.NS", "ICICIBANK.NS", "KOTAKBANK.NS"],
    "Automobiles": ["TATAMOTORS.NS", "MARUTI.NS"],
    "Pharma": ["SUNPHARMA.NS", "CIPLA.NS"],
    "FMCG": ["ITC.NS", "HINDUNILVR.NS"],
    "Metals": ["TATASTEEL.NS"]
}

# --- Stock level average trading volumes ---
avg_volumes = df.groupby("ticker")["volume"].mean().sort_values(ascending=False)

plt.figure(figsize=(12,6))
avg_volumes.plot(kind="bar", color="skyblue")
plt.title("Average Trading Volume per Stock")
plt.ylabel("Average Volume")
plt.xticks(rotation=45)
plt.tight_layout()
stock_chart = os.path.join(OUTPUT_DIR, "avg_volume_per_stock.png")
plt.savefig(stock_chart)
plt.close()
print(f"✅ Saved: {stock_chart}")

# --- Sector level average trading volumes ---
sector_avg = {}
for sector, tickers in sectors.items():
    sector_data = df[df["ticker"].isin(tickers)]
    sector_avg[sector] = sector_data["volume"].mean()

sector_avg = pd.Series(sector_avg).sort_values(ascending=False)

plt.figure(figsize=(10,5))
sector_avg.plot(kind="bar", color="orange")
plt.title("Average Trading Volume per Sector")
plt.ylabel("Average Volume")
plt.xticks(rotation=45)
plt.tight_layout()
sector_chart = os.path.join(OUTPUT_DIR, "avg_volume_per_sector.png")
plt.savefig(sector_chart)
plt.close()
print(f"✅ Saved: {sector_chart}")
