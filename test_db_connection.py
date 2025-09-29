from db_connection import get_engine

engine = get_engine()

try:
    # Attempt to connect
    conn = engine.connect()
    print("✅ Connection to PostgreSQL successful!")
    conn.close()
except Exception as e:
    print("❌ Connection failed:", e)
