# Stock ETL & Analysis Project
## 📌 Project Overview

This project extracts, transforms, and analyzes historical stock data for multiple companies. It includes:

ETL pipeline: Fetch data from Yahoo Finance, clean it, and load into PostgreSQL.

Analysis scripts: Perform multiple financial analyses and generate charts and tables.

Outputs: All results are saved in the outputs/ folder, organized by analysis type.


## 🗂 Folder Structure

```text
stock-etl/
├── data/
│   ├── raw/              # Raw downloaded stock CSVs
│   └── cleaned/          # Cleaned CSVs ready for DB
├── outputs/              # Analysis results (images & CSVs)
│   ├── analyze_data/
│   ├── correlation_volatility/
│   ├── cumulative_returns/
│   ├── drawdowns/
│   ├── moving_average_crossovers/
│   ├── return_vs_volatility/
│   ├── sector_daily_returns/
│   ├── sector_trends/
│   ├── top_movers_sector_summary/
│   ├── trading_volume_analysis/
│   └── volatility_vs_return/
├── venv/                 # Python virtual environment
├── analyze_data.py
├── check_cleaned.py
├── clean_data.py
├── correlation_volatility.py
├── cumulative_returns.py
├── db_connection.py
├── drawdowns.py
├── export_summary_tables.py
├── fetch_data.py
├── load_to_db.py
├── moving_average_crossovers.py
├── return_vs_volatility.py
├── seasonality_analysis.py
├── sector_daily_returns.py
├── sector_trends.py
├── test_db_connection.py
├── top_movers_sector_summary.py
├── trading_volume_analysis.py
└── volatility_vs_return.py
```

## 🛠 Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone <your-github-repo-url>
cd stock-etl
```
### 2️⃣ Create & Activate Virtual Environment
```bash
python -m venv venv
Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3️⃣ Install Required Packages

```bash
pip install -r requirements.txt


Typical packages included: pandas, numpy, matplotlib, seaborn, sqlalchemy, psycopg2-binary, yfinance.
```

### 4️⃣ Setup PostgreSQL Database
```bash
Start PostgreSQL server.

Create a new database:

CREATE DATABASE stock_etl;


Update database credentials in db_connection.py if needed:

DATABASE = "stock_etl"
USER = "postgres"
PASSWORD = "admin"
HOST = "localhost"
PORT = "5432"
```
### 5️⃣ Test Database Connection
```bash
python test_db_connection.py


✅ Should print: Connection successful!
```
## ⚡ Workflow

```bash
Step 1: Fetch & Clean Data

fetch_data.py → Downloads historical stock data to data/raw/.

clean_data.py → Cleans raw CSVs and saves to data/cleaned/.

check_cleaned.py → Quick inspection of cleaned files.

Step 2: Load Data into Database

load_to_db.py → Loads cleaned CSVs into PostgreSQL table stock_data.

Step 3: Run Analyses

Each analysis script saves outputs into its dedicated folder in outputs/.
```
## Script	Description
```bash
analyze_data.py	Average daily returns, closing price trends, and daily return histograms.
sector_trends.py	Closing price trends per sector.
sector_daily_returns.py	Daily return comparison per sector.
correlation_volatility.py	Correlation heatmap & rolling volatility of stocks.
top_movers_sector_summary.py	Top/bottom 5 movers & sector average returns.
moving_average_crossovers.py	Detects moving average crossover signals.
return_vs_volatility.py	Plots return vs volatility scatter for stocks.
volatility_vs_return.py	Another variant of risk-return scatter analysis.
trading_volume_analysis.py	Average trading volume per stock & sector.
drawdowns.py	Maximum drawdown per stock (risk measure).
cumulative_returns.py	Cumulative returns chart for all stocks.
seasonality_analysis.py	Monthly/quarterly return patterns.
export_summary_tables.py	Exports key summary tables (returns, volatility, etc.) to CSV.
```
## ✅ Notes

All outputs are stored in outputs/<script_name>/ folders.

Each script is independent and can be executed separately.

The project is modular; new analyses can be added by following the same structure.
