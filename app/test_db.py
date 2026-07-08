# =============================================================================
# test_db.py — a tiny script to check that the database connection works.
#
# Run this from the project root with:  python -m app.test_db
# If it prints a list of patients, then db.py + Docker + PostgreSQL are all
# talking to each other correctly. It's a quick "sanity check" before touching
# the GUI in main.py.
# =============================================================================

from app.db import fetch_all   # reuse the same read helper the GUI uses

# Run a SELECT and get back a list of dict rows (one dict per patient).
rows = fetch_all("SELECT patient_id, first_name, last_name FROM patients")

# Loop over the rows and print each patient on its own line.
# row["first_name"] works because db.py uses RealDictCursor (dict rows).
for row in rows:
    print(f"{row['patient_id']}: {row['first_name']} {row['last_name']}")

# len(rows) = how many rows the query returned = number of patients found.
print(f"\nTotal: {len(rows)} patients")
