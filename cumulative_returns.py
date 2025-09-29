import pandas as pd
import matplotlib.pyplot as plt
import os
from db_connection import get_engine

# -----------------------------
# Create outputs folder
# -----------------------------
OUTPUT_DIR = os.path.join("outputs", "cumulative_returns")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# -----------------------------
# Connect to database
# -----------------------------
engine = get_engine()

# Fetch all data
df = pd.read_sql("SELECT * FROM stock_data", engine)
df['date'] = pd.to_datetime(df['date'])

# -----------------------------
# Calculate cumulative returns
# -----------------------------
returns = df.pivot(index="date", columns="ticker", values="daily_return").fillna(0)
cumulative = (1 + returns).cumprod()

# -----------------------------
# Plot cumulative returns
# -----------------------------
plt.figure(figsize=(14,8))
for col in cumulative.columns:
    plt.plot(cumulative.index, cumulative[col], label=col)

plt.title("Cumulative Returns (₹1 invested)")
plt.xlabel("Date")
plt.ylabel("Growth of ₹1")
plt.legend()
plt.tight_layout()

chart_file = os.path.join(OUTPUT_DIR, "cumulative_returns.png")
plt.savefig(chart_file)
plt.close()
print(f"✅ Saved cumulative returns chart: {chart_file}")

# -----------------------------
# Save cumulative returns table
# -----------------------------
csv_file = os.path.join(OUTPUT_DIR, "cumulative_returns.csv")
cumulative.to_csv(csv_file)
print(f"✅ Saved cumulative returns table: {csv_file}")
