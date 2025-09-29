import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from db_connection import get_engine

# -----------------------------
# Create outputs folder for this script
# -----------------------------
OUTPUT_DIR = "outputs/correlation_volatility"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# -----------------------------
# Connect to database
# -----------------------------
engine = get_engine()

# Fetch all data
df = pd.read_sql("SELECT * FROM stock_data", engine)
df['date'] = pd.to_datetime(df['date'])

# -----------------------------
# Prepare data for analysis
# -----------------------------
# Pivot to have tickers as columns for daily returns
daily_returns = df.pivot(index='date', columns='ticker', values='daily_return')

# -----------------------------
# 1️⃣ Correlation Heatmap
# -----------------------------
corr_matrix = daily_returns.corr()

plt.figure(figsize=(12,10))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", cbar=True)
plt.title("Correlation Matrix of Daily Returns")
plt.tight_layout()
heatmap_file = os.path.join(OUTPUT_DIR, "daily_returns_correlation.png")
plt.savefig(heatmap_file)
plt.show()
print(f"✅ Saved correlation heatmap: {heatmap_file}")

# -----------------------------
# 2️⃣ Volatility Analysis (Rolling Std Dev)
# -----------------------------
volatility = daily_returns.rolling(window=20).std()  # 20-day rolling volatility

plt.figure(figsize=(14,8))
for col in volatility.columns:
    plt.plot(volatility.index, volatility[col], label=col)
plt.title("20-Day Rolling Volatility of Daily Returns")
plt.xlabel("Date")
plt.ylabel("Volatility")
plt.legend()
plt.tight_layout()
vol_file = os.path.join(OUTPUT_DIR, "rolling_volatility.png")
plt.savefig(vol_file)
plt.show()
print(f"✅ Saved volatility chart: {vol_file}")

# -----------------------------
# 3️⃣ Save Correlation Table as CSV
# -----------------------------
corr_csv = os.path.join(OUTPUT_DIR, "correlation_matrix.csv")
corr_matrix.to_csv(corr_csv)
print(f"✅ Saved correlation table: {corr_csv}")
