import yfinance as yf
import os

# Create folder if not exists
os.makedirs("data/raw", exist_ok=True)

# 15 stock tickers across different sectors
tickers = [
    # Energy & Conglomerates
    "RELIANCE.NS",
    "ONGC.NS",
    
    # IT Services
    "TCS.NS",
    "INFY.NS",
    "WIPRO.NS",
    
    # Banking & Finance
    "HDFCBANK.NS",
    "ICICIBANK.NS",
    "KOTAKBANK.NS",
    
    # Automobiles
    "TATAMOTORS.NS",
    "MARUTI.NS",
    
    # Pharma
    "SUNPHARMA.NS",
    "CIPLA.NS",
    
    # FMCG
    "ITC.NS",
    "HINDUNILVR.NS",
    
    # Metals
    "TATASTEEL.NS"
]

# Download historical data
for ticker in tickers:
    print(f"Fetching {ticker}...")
    df = yf.download(ticker, start="2023-01-01", end="2025-09-30")
    if not df.empty:
        df.reset_index(inplace=True)  # ensure 'Date' column
        file_path = f"data/raw/{ticker}.csv"
        df.to_csv(file_path, index=False)
        print(f"✅ Saved: {file_path}")
    else:
        print(f"⚠️ No data found for {ticker}")
