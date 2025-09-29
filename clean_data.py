import pandas as pd
import os

# Input & Output folders
RAW_DIR = "data/raw"
CLEAN_DIR = "data/cleaned"

# Create cleaned folder if not exists
os.makedirs(CLEAN_DIR, exist_ok=True)

# Loop through all raw CSV files
for file in os.listdir(RAW_DIR):
    if file.endswith(".csv"):
        file_path = os.path.join(RAW_DIR, file)
        print(f"Cleaning {file}...")

        # Load data
        df = pd.read_csv(file_path)

        # Standardize column names
        df.columns = [col.strip().title().replace(" ", "_") for col in df.columns]

        # Ensure Date column is datetime
        if "Date" in df.columns:
            df["Date"] = pd.to_datetime(df["Date"])

        # Convert numeric columns properly
        numeric_cols = ["Open", "High", "Low", "Close", "Adj_Close", "Volume"]
        for col in numeric_cols:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors="coerce")

        # Handle missing values (forward fill, then back fill)
        df = df.ffill().bfill()

        # Remove duplicates
        df.drop_duplicates(inplace=True)

        # Add calculated columns
        if "Open" in df.columns and "Close" in df.columns:
            df["Daily_Return"] = (df["Close"] - df["Open"]) / df["Open"]

        if "Close" in df.columns:
            df["MA_5"] = df["Close"].rolling(5).mean()
            df["MA_20"] = df["Close"].rolling(20).mean()

        # Save cleaned file
        clean_path = os.path.join(CLEAN_DIR, file)
        df.to_csv(clean_path, index=False)
        print(f"✅ Saved cleaned file: {clean_path}")
