import pandas as pd
import matplotlib.pyplot as plt
import os
from db_connection import get_engine

# -----------------------------
# Create outputs folder for this script
# -----------------------------
OUTPUT_DIR = "outputs/moving_average_crossovers"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# -----------------------------
# Connect to database
# -----------------------------
engine = get_engine()

# Fetch all data
df = pd.read_sql("SELECT * FROM stock_data", engine)
df['date'] = pd.to_datetime(df['date'])

# -----------------------------
# List of tickers
# -----------------------------
tickers = df['ticker'].unique()

# -----------------------------
# Process each stock
# -----------------------------
for ticker in tickers:
    stock_df = df[df['ticker'] == ticker].sort_values('date').copy()
    
    # Ensure MA_5 and MA_20 exist
    if 'ma_5' not in stock_df.columns or 'ma_20' not in stock_df.columns:
        stock_df['ma_5'] = stock_df['close'].rolling(5).mean()
        stock_df['ma_20'] = stock_df['close'].rolling(20).mean()
    
    # Generate signals
    stock_df['signal'] = 0
    stock_df.loc[stock_df['ma_5'] > stock_df['ma_20'], 'signal'] = 1  # Buy
    stock_df.loc[stock_df['ma_5'] < stock_df['ma_20'], 'signal'] = -1  # Sell

    # Plot closing price with MAs and signals
    plt.figure(figsize=(14,7))
    plt.plot(stock_df['date'], stock_df['close'], label='Close Price', color='blue')
    plt.plot(stock_df['date'], stock_df['ma_5'], label='MA 5', color='green', linestyle='--')
    plt.plot(stock_df['date'], stock_df['ma_20'], label='MA 20', color='red', linestyle='-.')
    
    # Plot Buy/Sell points
    plt.scatter(stock_df[stock_df['signal']==1]['date'], 
                stock_df[stock_df['signal']==1]['close'], 
                marker='^', color='green', s=100, label='Buy Signal')
    plt.scatter(stock_df[stock_df['signal']==-1]['date'], 
                stock_df[stock_df['signal']==-1]['close'], 
                marker='v', color='red', s=100, label='Sell Signal')
    
    plt.title(f"{ticker} - Moving Average Crossovers")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    
    # Save plot
    plot_file = os.path.join(OUTPUT_DIR, f"{ticker}_ma_crossovers.png")
    plt.savefig(plot_file)
    plt.show()
    print(f"✅ Saved plot: {plot_file}")
    
    # Save table with signals
    csv_file = os.path.join(OUTPUT_DIR, f"{ticker}_ma_signals.csv")
    stock_df[['date', 'close', 'ma_5', 'ma_20', 'signal']].to_csv(csv_file, index=False)
    print(f"✅ Saved signals table: {csv_file}")
