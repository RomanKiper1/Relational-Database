-- ============================================================================
-- 02_seed.sql — "seed" data: fills the empty patients table with test rows.
--
-- "Seeding" means loading sample/starter data so you have something to look at
-- while developing. This runs after 01_patients.sql (alphabetical order), so
-- the table already exists by the time we insert into it.
-- ============================================================================

-- One INSERT can add MANY rows: list the columns once, then give a
-- comma-separated tuple of values for each row. Note we do NOT provide
-- patient_id — it is SERIAL, so PostgreSQL assigns 1, 2, 3, ... automatically.
INSERT INTO patients (first_name, last_name, date_of_birth, gender, email, phone) VALUES
('John', 'Doe', '1990-01-15', 'M', 'john.doe@example.com', '123-456-7890'),
('Jane', 'Smith', '1985-07-20', 'F', 'jane.smith@example.com', '098-765-4321'),
('Emily', 'Johnson', '1992-03-10', 'F', 'emily.johnson@example.com', '111-222-3333'),
('David', 'Lee', '1988-11-25', 'M', 'david.lee@example.com', '222-333-4444'),
('Sarah', 'Wilson', '1995-06-18', 'F', 'sarah.wilson@example.com', '333-444-5555'),
('Michael', 'Brown', '1991-09-12', 'M', 'michael.brown@example.com', '444-555-6666'),
('Olivia', 'Davis', '1987-12-05', 'F', 'olivia.davis@example.com', '555-666-7777'),
('James', 'Miller', '1993-04-28', 'M', 'james.miller@example.com', '666-777-8888'),
('Ava', 'Garcia', '1989-08-14', 'F', 'ava.garcia@example.com', '777-888-9999'),
('William', 'Martinez', '1996-02-22', 'M', 'william.martinez@example.com', '888-999-0000'),
('Sophia', 'Hernandez', '1990-11-30', 'F', 'sophia.hernandez@example.com', '999-000-1111'),
('Daniel', 'Lopez', '1986-07-17', 'M', 'daniel.lopez@example.com', '000-111-2222'),
('Isabella', 'Gonzalez', '1994-03-08', 'F', 'isabella.gonzalez@example.com', '111-222-3333'),
('Joseph', 'Perez', '1992-10-24', 'M', 'joseph.perez@example.com', '222-333-4444');
