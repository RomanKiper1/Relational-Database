CREATE TABLE appointments (
    appointment_id SERIAL PRIMARY KEY,
    patient_id INT NOT NULL,
    staff_id INT NOT NULL,
    appointment_date DATE NOT NULL,
    appointment_time TIME NOT NULL,
    appointment_type VARCHAR(50) NOT NULL,
    appointment_status VARCHAR(50) NOT NULL,
    appointment_notes TEXT,
    appointment_created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    appointment_updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO appointments (patient_id, staff_id, appointment_date, appointment_time, appointment_type, appointment_status, appointment_notes) VALUES
(1, 1, '2026-01-01', '10:00:00', 'Consultation', 'Confirmed', 'Follow-up appointment'),
(2, 2, '2026-01-02', '11:00:00', 'Check-up', 'Confirmed', 'Annual check-up'),
(3, 3, '2026-01-03', '12:00:00', 'Treatment', 'Confirmed', 'Routine treatment'),
(4, 4, '2026-01-04', '13:00:00', 'Consultation', 'Confirmed', 'Follow-up appointment'),
(5, 5, '2026-01-05', '14:00:00', 'Check-up', 'Confirmed', 'Annual check-up'),
(6, 6, '2026-01-06', '15:00:00', 'Treatment', 'Confirmed', 'Routine treatment'),
(7, 7, '2026-01-07', '16:00:00', 'Consultation', 'Confirmed', 'Follow-up appointment'),
(8, 8, '2026-01-08', '17:00:00', 'Check-up', 'Confirmed', 'Annual check-up'),
(9, 9, '2026-01-09', '18:00:00', 'Treatment', 'Confirmed', 'Routine treatment'),
(10, 10, '2026-01-10', '19:00:00', 'Consultation', 'Confirmed', 'Follow-up appointment');