## Stock ETL & Analysis Project
# Project Overview

This project extracts, transforms, and analyzes historical stock data for multiple companies. It includes:

ETL pipeline: Fetch data from Yahoo Finance, clean it, and load into PostgreSQL.

Analysis scripts: Perform multiple financial analyses and generate charts and tables.

Outputs: All results are saved in the outputs/ folder, organized by analysis type.


# 🗂 Folder Structure

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
