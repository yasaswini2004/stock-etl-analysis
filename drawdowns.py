import pandas as pd
import matplotlib.pyplot as plt
import os
from db_connection import get_engine

# -----------------------------
# Create outputs folder
# -----------------------------
OUTPUT_DIR = os.path.join("outputs", "drawdowns")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# -----------------------------
# Connect to database
# -----------------------------
engine = get_engine()

# Fetch all data
df = pd.read_sql("SELECT * FROM stock_data", engine)
df['date'] = pd.to_datetime(df['date'])

# -----------------------------
# Calculate cumulative returns per stock
# -----------------------------
cum_returns = df.pivot(index="date", columns="ticker", values="daily_return").fillna(0)
cum_returns = (1 + cum_returns).cumprod()

# -----------------------------
# Calculate drawdowns
# -----------------------------
drawdowns = {}
for ticker in cum_returns.columns:
    series = cum_returns[ticker]
    rolling_max = series.cummax()
    dd = (series / rolling_max - 1)  # drawdown %
    drawdowns[ticker] = dd.min()     # max drawdown (most negative)

drawdowns = pd.Series(drawdowns).sort_values()

# -----------------------------
# Plot drawdowns
# -----------------------------
plt.figure(figsize=(12,6))
drawdowns.plot(kind="bar", color="red", edgecolor="black")
plt.title("Maximum Drawdown per Stock")
plt.ylabel("Max Drawdown (%)")
plt.xticks(rotation=45)
plt.tight_layout()
chart_file = os.path.join(OUTPUT_DIR, "max_drawdown_per_stock.png")
plt.savefig(chart_file)
plt.close()
print(f"✅ Saved drawdown chart: {chart_file}")

# -----------------------------
# Save drawdowns as CSV
# -----------------------------
csv_file = os.path.join(OUTPUT_DIR, "max_drawdown_per_stock.csv")
drawdowns.to_csv(csv_file, header=["max_drawdown"])
print(f"✅ Saved drawdown table: {csv_file}")
