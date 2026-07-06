import os
from pathlib import Path

import psycopg2
from dotenv import load_dotenv
from psycopg2.extras import RealDictCursor

# Loading .env from dir level up than app/
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

#layer 2 - connection function, open a connection to DB, like "give a call" to DB
def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432"),
        dbname=os.getenv("DB_NAME", "clinic_db"),
        user=os.getenv("DB_USER", "clinic_user"),
        password=os.getenv("DB_PASSWORD"),
        cursor_factory=RealDictCursor,
    )

#Layer fetch_all for SELECT
def fetch_all(query, params=None):
    conn=get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(query, params or ())
            return cur.fetchall()
    finally:
        conn.close()

#Layer 4 execute for INSERT/UPDATE/DELETE

def execute(query, params=None):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(query, params or ())
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()