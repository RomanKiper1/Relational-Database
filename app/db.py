# =============================================================================
# db.py  — the "database access layer" of the app.
#
# The whole point of this file is to keep ALL PostgreSQL details in one place.
# The rest of the program (main.py, test_db.py) never talks to psycopg2
# directly; it only calls the small helper functions defined here:
#     get_connection()  -> open a connection
#     fetch_all(query)  -> run a SELECT and get rows back
#     execute(query)    -> run INSERT / UPDATE / DELETE and save the change
# This separation is a common pattern: the "data layer" hides the messy
# connection code behind a few clean functions.
# =============================================================================

import os                       # read environment variables (os.getenv)
from pathlib import Path        # build file paths in an OS-independent way

import psycopg2                             # the PostgreSQL driver ("connector") for Python
from dotenv import load_dotenv             # loads variables from a .env file into the environment
from psycopg2.extras import RealDictCursor  # makes query results come back as dicts (see below)

# Load the .env file so that os.getenv() below can see DB_HOST, DB_PASSWORD, etc.
# We build the path step by step:
#   __file__                -> path of THIS file (.../app/db.py)
#   .resolve()              -> turn it into a full absolute path
#   .parent                 -> the folder containing it       (.../app)
#   .parent.parent          -> one folder higher, the project root
#   / ".env"                -> add the .env filename to that folder
# So the .env file is expected to live in the project root, next to app/.
load_dotenv(Path(__file__).resolve().parent.parent / ".env")


# --- Layer 1: connection --------------------------------------------------
# Opens a fresh connection to the database. Think of a connection as
# "picking up the phone and calling the database server".
def get_connection():
    return psycopg2.connect(
        # os.getenv("KEY", "default") reads an environment variable, and if it
        # is missing, falls back to the default value given as second argument.
        host=os.getenv("DB_HOST", "localhost"),   # where the DB server runs
        port=os.getenv("DB_PORT", "5432"),        # 5432 = PostgreSQL's default port
        dbname=os.getenv("DB_NAME", "clinic_db"), # which database to use
        user=os.getenv("DB_USER", "clinic_user"), # which user to log in as
        password=os.getenv("DB_PASSWORD"),        # no default: the password must come from .env
        # By default psycopg2 returns each row as a plain tuple, e.g. (1, "John").
        # RealDictCursor makes each row a dictionary instead, e.g.
        #     {"patient_id": 1, "first_name": "John"}
        # That is why elsewhere we can write row["first_name"] instead of row[1].
        cursor_factory=RealDictCursor,
    )


# --- Layer 2: read helper (for SELECT) ------------------------------------
# Runs a SELECT query and returns ALL matching rows as a list of dicts.
# `params` are values to safely inject into the query (see note below).
def fetch_all(query, params=None):
    conn = get_connection()           # open the connection
    try:
        # `with conn.cursor() as cur:` creates a cursor (the object that runs
        # SQL and holds the result). The `with` block automatically closes the
        # cursor when we leave it, even if an error happens.
        with conn.cursor() as cur:
            # Passing params separately (instead of pasting them into the query
            # string) lets psycopg2 escape them. This is how you PREVENT SQL
            # injection. `params or ()` means: use params if given, else an
            # empty tuple () so execute() always gets a valid value.
            cur.execute(query, params or ())
            return cur.fetchall()     # fetchall() -> list of all result rows
    finally:
        # `finally` runs no matter what (success OR error), so the connection
        # is always closed and we don't leak open connections.
        conn.close()


# --- Layer 3: write helper (for INSERT / UPDATE / DELETE) ------------------
# Runs a query that CHANGES data. Unlike a SELECT, changes must be committed
# (saved) before they become permanent in the database.
def execute(query, params=None):
    conn = get_connection()               # open the connection ("call" the DB)
    try:
        with conn.cursor() as cur:        # get a cursor; auto-closed after the block
            cur.execute(query, params or ())  # run the SQL (still not saved yet!)
        conn.commit()                     # COMMIT = permanently save the change
    except Exception:
        # If anything went wrong, ROLLBACK undoes every change made in this
        # transaction, leaving the database exactly as it was before.
        conn.rollback()
        raise                             # re-raise the error so the caller/terminal sees it
    finally:
        conn.close()                      # always close, success or failure
