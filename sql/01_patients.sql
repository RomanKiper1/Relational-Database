-- Table of patients
CREATE TABLE patients (
    patient_id SERIAL PRIMARY KEY, -- Unique identifier for each patient
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE,
    gender CHAR(1) CHECK (gender IN ('M', 'F')), -- 'M' for male, 'F' for female
    email VARCHAR(255),
    phone VARCHAR(30)
);