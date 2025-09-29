import pandas as pd
import matplotlib.pyplot as plt
import os
from db_connection import get_engine

# ------------------------------
# Dedicated folder for this script's outputs
OUTPUT_DIR = "outputs/sector_daily_returns"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ------------------------------
# Connect to database
engine = get_engine()

# Fetch all data
df = pd.read_sql("SELECT * FROM stock_data", engine)
df['date'] = pd.to_datetime(df['date'])

# ------------------------------
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

# ------------------------------
# Plot daily returns per sector
for sector_name, tickers in sectors.items():
    plt.figure(figsize=(12,6))
    
    for ticker in tickers:
        stock_df = df[df['ticker'] == ticker].sort_values('date')
        if not stock_df.empty:
            plt.plot(stock_df['date'], stock_df['daily_return'], label=ticker)
    
    plt.title(f"{sector_name} - Daily Returns Comparison")
    plt.xlabel("Date")
    plt.ylabel("Daily Return")
    plt.axhline(0, color='black', linestyle='--', linewidth=1)  # zero line reference
    plt.legend()
    plt.tight_layout()
    
    # Save chart in sector_daily_returns folder
    output_file = os.path.join(OUTPUT_DIR, f"{sector_name.replace(' ','_')}_daily_returns.png")
    plt.savefig(output_file)
    plt.show()
    print(f"✅ Saved: {output_file}")
