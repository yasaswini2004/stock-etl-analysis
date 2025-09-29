import pandas as pd
import matplotlib.pyplot as plt
import os
from db_connection import get_engine

# ------------------------------
# Create a dedicated folder for this script's outputs
OUTPUT_DIR = "outputs/analyze_data"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ------------------------------
# Connect to database
engine = get_engine()

# Fetch all data
df = pd.read_sql("SELECT * FROM stock_data", engine)
df['date'] = pd.to_datetime(df['date'])

# ------------------------------
# 1️⃣ Average Daily Return by Stock
avg_returns = df.groupby('ticker')['daily_return'].mean().sort_values(ascending=False)
print("Average Daily Returns:\n", avg_returns)

plt.figure(figsize=(12,6))
avg_returns.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Average Daily Return by Stock')
plt.ylabel('Average Daily Return')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "avg_daily_return.png"))
plt.show()

# ------------------------------
# 2️⃣ Closing Price Trends (example: RELIANCE.NS)
reliance = df[df['ticker']=='RELIANCE.NS'].sort_values('date')

plt.figure(figsize=(12,6))
plt.plot(reliance['date'], reliance['close'], label='Close Price')
plt.plot(reliance['date'], reliance['ma_5'], label='MA 5', linestyle='--')
plt.plot(reliance['date'], reliance['ma_20'], label='MA 20', linestyle='-.')
plt.title('RELIANCE.NS Closing Price & Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "reliance_trend.png"))
plt.show()

# ------------------------------
# 3️⃣ Daily Returns Histogram
plt.figure(figsize=(10,5))
df['daily_return'].hist(bins=50, color='lightgreen', edgecolor='black')
plt.title('Histogram of Daily Returns (All Stocks)')
plt.xlabel('Daily Return')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "daily_return_histogram.png"))
plt.show()
