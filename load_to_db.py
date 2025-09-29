import pandas as pd
import os
from db_connection import get_engine

CLEAN_DIR = "data/cleaned"
engine = get_engine()

# Loop through all cleaned CSV files
for file in os.listdir(CLEAN_DIR):
    if file.endswith(".csv"):
        file_path = os.path.join(CLEAN_DIR, file)
        print(f"Loading {file} into database...")

        # Load CSV
        df = pd.read_csv(file_path)

        # Add ticker column from filename
        ticker = file.replace(".csv", "")
        df["ticker"] = ticker

        # Reorder columns to match table
        df = df[["ticker", "Date", "Open", "High", "Low", "Close", "Volume", "Daily_Return", "MA_5", "MA_20"]]

        # Rename columns to match PostgreSQL table (lowercase)
        df.columns = ["ticker", "date", "open", "high", "low", "close", "volume", "daily_return", "ma_5", "ma_20"]

        # Insert into PostgreSQL
        df.to_sql("stock_data", engine, if_exists="append", index=False)
        print(f"✅ Loaded {file} into stock_data table")
