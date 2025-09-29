import pandas as pd
import matplotlib.pyplot as plt
import os
from db_connection import get_engine

# -----------------------------
# Create outputs folder
# -----------------------------
OUTPUT_DIR = os.path.join("outputs", "seasonality_analysis")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# -----------------------------
# Connect to database
# -----------------------------
engine = get_engine()

# Fetch all data
df = pd.read_sql("SELECT * FROM stock_data", engine)
df['date'] = pd.to_datetime(df['date'])

# Pivot daily returns
returns = df.pivot(index='date', columns='ticker', values='daily_return').fillna(0)

# -----------------------------
# Monthly seasonality
# -----------------------------
monthly_returns = returns.groupby(returns.index.to_period('M')).mean()

plt.figure(figsize=(14,8))
for col in monthly_returns.columns:
    plt.plot(monthly_returns.index.to_timestamp(), monthly_returns[col], label=col)
plt.title("Monthly Average Daily Returns")
plt.xlabel("Month")
plt.ylabel("Average Daily Return")
plt.legend()
plt.tight_layout()

monthly_file = os.path.join(OUTPUT_DIR, "monthly_avg_daily_returns.png")
plt.savefig(monthly_file)
plt.close()
print(f"✅ Saved monthly returns chart: {monthly_file}")

monthly_csv = os.path.join(OUTPUT_DIR, "monthly_avg_daily_returns.csv")
monthly_returns.to_csv(monthly_csv)
print(f"✅ Saved monthly returns table: {monthly_csv}")

# -----------------------------
# Quarterly seasonality
# -----------------------------
quarterly_returns = returns.groupby(returns.index.to_period('Q')).mean()

plt.figure(figsize=(14,8))
for col in quarterly_returns.columns:
    plt.plot(quarterly_returns.index.to_timestamp(), quarterly_returns[col], label=col)
plt.title("Quarterly Average Daily Returns")
plt.xlabel("Quarter")
plt.ylabel("Average Daily Return")
plt.legend()
plt.tight_layout()

quarterly_file = os.path.join(OUTPUT_DIR, "quarterly_avg_daily_returns.png")
plt.savefig(quarterly_file)
plt.close()
print(f"✅ Saved quarterly returns chart: {quarterly_file}")

quarterly_csv = os.path.join(OUTPUT_DIR, "quarterly_avg_daily_returns.csv")
quarterly_returns.to_csv(quarterly_csv)
print(f"✅ Saved quarterly returns table: {quarterly_csv}")
