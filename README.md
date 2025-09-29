📌 Project Overview

This project extracts, transforms, and analyzes historical stock data for multiple companies. It includes:

ETL pipeline: Fetch data from Yahoo Finance, clean it, and load into PostgreSQL.

Analysis scripts: Perform multiple financial analyses and generate charts and tables.

Outputs: All results are saved in the outputs/ folder, organized by analysis type.

🗂 Folder Structure
stock-etl/
│
├── data/
│   ├── raw/              # Raw downloaded stock CSVs
│   └── cleaned/          # Cleaned CSVs ready for DB
│
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
│
├── venv/                 # Python virtual environment
│
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

🛠 Setup Instructions

Clone the repository

git clone https://github.com/<username>/stock-etl-analysis.git
cd stock-etl-analysis


Create a Python virtual environment

python -m venv venv
venv\Scripts\activate   # Windows
# or
source venv/bin/activate # Mac/Linux


Install required packages

pip install -r requirements.txt


(Create requirements.txt with all needed libraries: pandas, yfinance, matplotlib, seaborn, sqlalchemy, psycopg2)

Set up PostgreSQL

Create database: stock_etl

Update credentials in db_connection.py if needed

Test connection:

python test_db_connection.py


Fetch & clean data

python fetch_data.py
python clean_data.py


Load cleaned data into DB

python load_to_db.py


Run analysis scripts
Each script generates its own output folder inside outputs/:

python analyze_data.py
python correlation_volatility.py
python cumulative_returns.py
python drawdowns.py
python moving_average_crossovers.py
python return_vs_volatility.py
python seasonality_analysis.py
python sector_daily_returns.py
python sector_trends.py
python top_movers_sector_summary.py
python trading_volume_analysis.py
python volatility_vs_return.py

📊 Analyses Included

Average daily returns per stock

Closing price trends

Daily returns histogram

Sector-wise trends & returns

Moving average crossovers

Return vs volatility

Correlation matrix & rolling volatility

Top & bottom movers by daily return

Trading volume analysis

Max drawdowns (risk measure)

Cumulative returns

Seasonality analysis (monthly/quarterly patterns)

Export summary tables (returns, volatility, etc.)

✅ Notes

Outputs are saved as PNG charts and CSV tables in the outputs/ folder.

Each analysis script has its own folder in outputs/ for organization.

Data cleaning handles missing values, duplicates, and numeric conversions.

Analyses are modular — you can run scripts independently.
