from app.db import get_db, insert_one

db = get_db()

if db.patients.count_documents({}) == 0:
    patients = patients = [
    {"patient_id": 1,  "first_name": "John",     "last_name": "Doe",        "date_of_birth": "1990-01-15", "gender": "M", "email": "john.doe@example.com",           "phone": "123-456-7890"},
    {"patient_id": 2,  "first_name": "Jane",     "last_name": "Smith",      "date_of_birth": "1985-07-20", "gender": "F", "email": "jane.smith@example.com",         "phone": "098-765-4321"},
    {"patient_id": 3,  "first_name": "Emily",    "last_name": "Johnson",    "date_of_birth": "1992-03-10", "gender": "F", "email": "emily.johnson@example.com",      "phone": "111-222-3333"},
    {"patient_id": 4,  "first_name": "David",    "last_name": "Lee",        "date_of_birth": "1988-11-25", "gender": "M", "email": "david.lee@example.com",          "phone": "222-333-4444"},
    {"patient_id": 5,  "first_name": "Sarah",    "last_name": "Wilson",     "date_of_birth": "1995-06-18", "gender": "F", "email": "sarah.wilson@example.com",       "phone": "333-444-5555"},
    {"patient_id": 6,  "first_name": "Michael",  "last_name": "Brown",      "date_of_birth": "1991-09-12", "gender": "M", "email": "michael.brown@example.com",      "phone": "444-555-6666"},
    {"patient_id": 7,  "first_name": "Olivia",   "last_name": "Davis",      "date_of_birth": "1987-12-05", "gender": "F", "email": "olivia.davis@example.com",         "phone": "555-666-7777"},
    {"patient_id": 8,  "first_name": "James",    "last_name": "Miller",     "date_of_birth": "1993-04-28", "gender": "M", "email": "james.miller@example.com",       "phone": "666-777-8888"},
    {"patient_id": 9,  "first_name": "Ava",      "last_name": "Garcia",     "date_of_birth": "1989-08-14", "gender": "F", "email": "ava.garcia@example.com",         "phone": "777-888-9999"},
    {"patient_id": 10, "first_name": "William",  "last_name": "Martinez",   "date_of_birth": "1996-02-22", "gender": "M", "email": "william.martinez@example.com",   "phone": "888-999-0000"},
    {"patient_id": 11, "first_name": "Sophia",   "last_name": "Hernandez",  "date_of_birth": "1990-11-30", "gender": "F", "email": "sophia.hernandez@example.com",   "phone": "999-000-1111"},
    {"patient_id": 12, "first_name": "Daniel",   "last_name": "Lopez",      "date_of_birth": "1986-07-17", "gender": "M", "email": "daniel.lopez@example.com",       "phone": "000-111-2222"},
    {"patient_id": 13, "first_name": "Isabella", "last_name": "Gonzalez",   "date_of_birth": "1994-03-08", "gender": "F", "email": "isabella.gonzalez@example.com",  "phone": "111-222-3333"},
    {"patient_id": 14, "first_name": "Joseph",   "last_name": "Perez",      "date_of_birth": "1992-10-24", "gender": "M", "email": "joseph.perez@example.com",       "phone": "222-333-4444"},
]
    db.patients.insert_many(patients)

if db.staff.count_documents({}) == 0:
    staff = [
        {"staff_id": 1,  "first_name": "Anna",   "last_name": "Lindstrom",  "email": "a.lindstrom@clinic.se",  "role": "gp_doctor",   "specialty": "General Practice"},
        {"staff_id": 2,  "first_name": "Erik",   "last_name": "Bergman",    "email": "e.bergman@clinic.se",    "role": "gp_doctor",   "specialty": "General Practice"},
        {"staff_id": 3,  "first_name": "Maria",  "last_name": "Johansson",  "email": "m.johansson@clinic.se",  "role": "gp_doctor",   "specialty": "General Practice"},
        {"staff_id": 4,  "first_name": "Lars",   "last_name": "Nilsson",    "email": "l.nilsson@clinic.se",    "role": "gp_doctor",   "specialty": "General Practice"},
        {"staff_id": 5,  "first_name": "Sofia",  "last_name": "Karlsson",   "email": "s.karlsson@clinic.se",   "role": "gp_doctor",   "specialty": "General Practice"},
        {"staff_id": 6,  "first_name": "Henrik", "last_name": "Andersson",  "email": "h.andersson@clinic.se",  "role": "specialist",  "specialty": "Cardiology"},
        {"staff_id": 7,  "first_name": "Elena",  "last_name": "Petrova",    "email": "e.petrova@clinic.se",    "role": "specialist",  "specialty": "Neurology"},
        {"staff_id": 8,  "first_name": "James",  "last_name": "Miller",     "email": "j.miller@clinic.se",     "role": "specialist",  "specialty": "Orthopedics"},
        {"staff_id": 9,  "first_name": "Yuki",   "last_name": "Tanaka",     "email": "y.tanaka@clinic.se",     "role": "specialist",  "specialty": "Dermatology"},
        {"staff_id": 10, "first_name": "Fatima", "last_name": "Hassan",     "email": "f.hassan@clinic.se",     "role": "specialist",  "specialty": "Oncology"},
        {"staff_id": 11, "first_name": "Oliver", "last_name": "Brown",      "email": "o.brown@clinic.se",      "role": "specialist",  "specialty": "Urology"},
        {"staff_id": 12, "first_name": "Ingrid", "last_name": "Svensson",   "email": "i.svensson@clinic.se",   "role": "specialist",  "specialty": "Gynecology"},
        {"staff_id": 13, "first_name": "Marcus", "last_name": "Weber",      "email": "m.weber@clinic.se",      "role": "specialist",  "specialty": "Radiology"},
        {"staff_id": 14, "first_name": "Lisa",   "last_name": "Ek",         "email": "l.ek@clinic.se",         "role": "nurse"},
        {"staff_id": 15, "first_name": "Tom",    "last_name": "Holm",       "email": "t.holm@clinic.se",       "role": "nurse"},
        {"staff_id": 16, "first_name": "Karin",  "last_name": "Dahl",       "email": "k.dahl@clinic.se",       "role": "janitor"},
        {"staff_id": 17, "first_name": "Robert", "last_name": "Strom",      "email": "r.finance@clinic.se",    "role": "cfo"},
        {"staff_id": 18, "first_name": "Helena", "last_name": "Smith",      "email": "h.books@outsource.se",   "role": "bookkeeper"},
        {"staff_id": 19, "first_name": "Nina",   "last_name": "Brooks",     "email": "n.contract@clinic.se",   "role": "contract_manager"},
    ]
    db.staff.insert_many(staff)

    print("Patients:", db.patients.count_documents({}))
    print(f"Inserted {len(staff)} staff")