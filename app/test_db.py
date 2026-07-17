# =============================================================================
# test_db.py — a tiny script to check that the database connection works.
#
# Run this from the project root with:  python -m app.test_db
# If it prints a list of patients, then db.py + Docker + PostgreSQL (migrated to MongoDB) are all
# talking to each other correctly. It's a quick "sanity check" before touching
# the GUI in main.py.
# =============================================================================

from app.db import get_db, find_all

db = get_db()

print("Connected to MongoDB!")
print("Collections:", db.list_collection_names())

patients = find_all("patients", sort=[("patient_id", 1)])
for row in patients[:5]:
    print(f"{row['patient_id']}: {row['first_name']} {row['last_name']}")

print(f"\nTotal: {len(patients)} patients")
