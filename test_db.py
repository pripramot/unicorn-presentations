import os
import pg8000.native
from dotenv import load_dotenv

load_dotenv()

DB_PASSWORD = os.getenv("SUPABASE_DB_PASSWORD")
DB_HOST = os.getenv("SUPABASE_DB_HOST")
DB_USER = os.getenv("SUPABASE_DB_USER", "postgres")
DB_PORT = int(os.getenv("SUPABASE_DB_PORT", "5432"))

print(f"Connecting to {DB_HOST} as {DB_USER}...")

try:
    conn = pg8000.native.Connection(
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        database="postgres",
        ssl_context=True
    )
    print("Connected!")
    results = conn.run("SELECT version();")
    print(f"Database Version: {results[0][0]}")
    conn.close()
    print("Success: God Mode (SQL) is active.")
except Exception as e:
    print(f"Connection Failed: {e}")
