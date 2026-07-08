-- ============================================================================
-- 03_staff.sql — defines and seeds the "staff" table (employees of the clinic).
--
-- Same idea as the patients files, but here the schema (CREATE TABLE) and the
-- data (INSERT) live together in one file. Runs third (alphabetical: 03_).
-- ============================================================================

-- Table of staff
CREATE TABLE staff (
    staff_id    SERIAL PRIMARY KEY,     -- auto-incrementing unique id per employee
    first_name  VARCHAR(100) NOT NULL,  -- required
    last_name   VARCHAR(100) NOT NULL,  -- required
    email       VARCHAR(255),           -- optional (may be NULL)
    role        VARCHAR(50) NOT NULL,   -- e.g. gp_doctor / specialist / nurse; later replace with ENUM
    specialty   VARCHAR(100)            -- only doctors have one; NULL for everyone else
);

-- Below are three separate INSERTs, grouped by staff type so it's easy to read.

-- 5 doctors (GP = General Practitioner). All have a specialty, so we list the
-- specialty column and give a value for it in every row.
INSERT INTO staff (first_name, last_name, email, role, specialty) VALUES
    ('Anna', 'Lindstrom', 'a.lindstrom@clinic.se', 'gp_doctor', 'General Practice'),
    ('Erik', 'Bergman', 'e.bergman@clinic.se', 'gp_doctor', 'General Practice'),
    ('Maria', 'Johansson', 'm.johansson@clinic.se', 'gp_doctor', 'General Practice'),
    ('Lars', 'Nilsson', 'l.nilsson@clinic.se', 'gp_doctor', 'General Practice'),
    ('Sofia', 'Karlsson', 's.karlsson@clinic.se', 'gp_doctor', 'General Practice');
-- Specialist doctors
INSERT INTO staff (first_name, last_name, email, role, specialty) VALUES
    ('Henrik', 'Andersson', 'h.andersson@clinic.se', 'specialist', 'Cardiology'),
    ('Elena', 'Petrova', 'e.petrova@clinic.se', 'specialist', 'Neurology'),
    ('James', 'Miller', 'j.miller@clinic.se', 'specialist', 'Orthopedics'),
    ('Yuki', 'Tanaka', 'y.tanaka@clinic.se', 'specialist', 'Dermatology'),
    ('Fatima', 'Hassan', 'f.hassan@clinic.se', 'specialist', 'Oncology'),
    ('Oliver', 'Brown', 'o.brown@clinic.se', 'specialist', 'Urology'),
    ('Ingrid', 'Svensson', 'i.svensson@clinic.se', 'specialist', 'Gynecology'),
    ('Marcus', 'Weber', 'm.weber@clinic.se', 'specialist', 'Radiology');

-- Non-doctor staff. Notice this INSERT omits the `specialty` column entirely,
-- so PostgreSQL stores NULL there for these rows (they have no specialty).
-- Nurses, janitor, CFO, accountant, contract managers, etc.
INSERT INTO staff (first_name, last_name, email, role) VALUES
    ('Lisa', 'Ek', 'l.ek@clinic.se', 'nurse'),
    ('Tom', 'Holm', 't.holm@clinic.se', 'nurse'),
    ('Karin', 'Dahl', 'k.dahl@clinic.se', 'janitor'),
    ('Robert', 'Strom', 'r.finance@clinic.se', 'cfo'),
    ('Helena', 'Smith', 'h.books@outsource.se', 'bookkeeper'),
    ('Nina', 'Brooks', 'n.contract@clinic.se', 'contract_manager');
