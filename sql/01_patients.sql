-- ============================================================================
-- 01_patients.sql — defines the "patients" table (its structure / schema).
--
-- Files in the sql/ folder run automatically the FIRST time the PostgreSQL
-- container starts (see docker-compose.yml). They run in alphabetical order,
-- which is why the names start with 01_, 02_, 03_ — to control the sequence.
-- In SQL, a comment starts with two dashes: --
-- ============================================================================

-- CREATE TABLE defines a new table and the columns (fields) it will hold.
CREATE TABLE patients (
    -- SERIAL = auto-incrementing integer: PostgreSQL fills in 1, 2, 3, ... for
    --          you, so you never set patient_id yourself on INSERT.
    -- PRIMARY KEY = this column uniquely identifies each row (no duplicates,
    --               never NULL). Every table should have one.
    patient_id SERIAL PRIMARY KEY,          -- Unique identifier for each patient

    -- VARCHAR(50) = text up to 50 characters long.
    -- NOT NULL    = this column is required; an INSERT without it is rejected.
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,

    -- No NOT NULL here, so these columns are OPTIONAL (may be left empty = NULL).
    date_of_birth DATE,                     -- DATE stores a calendar date (YYYY-MM-DD)

    -- CHAR(1)  = exactly one character.
    -- CHECK(...) = a rule the value must satisfy; here gender must be 'M' or 'F',
    --              otherwise PostgreSQL refuses to store the row.
    gender CHAR(1) CHECK (gender IN ('M', 'F')),  -- 'M' for male, 'F' for female
    email VARCHAR(255),
    phone VARCHAR(30)
);
