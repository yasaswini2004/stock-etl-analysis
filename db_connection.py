from sqlalchemy import create_engine

# Replace with your credentials
DATABASE = "stock_etl"
USER = "postgres"
PASSWORD = "admin"
HOST = "localhost"
PORT = "5432"

# Create engine
engine = create_engine(f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")

def get_engine():
    return engine
