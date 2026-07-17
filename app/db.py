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


from dotenv import load_dotenv             # loads variables from a .env file into the environment
from pymongo import MongoClient

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
load_dotenv(Path(__file__).resolve().parent.parent / ".env")
_client = None
def get_db():
    global _client
    if _client is None:
        uri = os.getenv("MONGODB_URI")
        if not uri:
            raise RuntimeError("MONGODB_URI is missing from .env")
        _client = MongoClient(uri)
    return _client[os.getenv("DB_NAME", "clinic_db")]
    
def find_all(collection, query=None, sort=None):
    """Like fetch_all — returns a list of dicts."""
    cursor = get_db()[collection].find(query or {})
    if sort:
        cursor = cursor.sort(sort)
    return list(cursor)

def insert_one(collection, document):
    """Like execute for INSERT."""
    get_db()[collection].insert_one(document)
    
def next_id(collection, field):
    """Simple auto-increment (replaces PostgreSQL SERIAL)."""
    last = get_db()[collection].find_one(sort=[(field, -1)])
    return (last[field] + 1) if last else 1
