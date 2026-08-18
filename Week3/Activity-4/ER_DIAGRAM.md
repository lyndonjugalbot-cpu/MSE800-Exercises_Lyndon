# ER Diagram — Student / Lecturer / Subject / Lecture / Enrollment
## Entities & attributes

- **Student**(`student_code` PK, first_name, last_name, gender, birth_date, address, email, phone_number)
- **Lecturer**(`lecturer_id` PK, first_name, last_name, email, address)
- **Subject**(`subject_code` PK, subject_name, subject_unit, subject_description)
- **Lecture**(`lecture_id` PK, `subject_code` FK → Subject, `lecturer_id` FK → Lecturer, lecture_name, room, day_time, capacity)
- **Enrollment**(`student_code` FK → Student, `lecture_id` FK → Lecture, enrollment_date, enrollment_status) — PK is `(student_code, lecture_id)`

## Relationships

- **Enrolls**: Student —(M:N via Enrollment)— Lecture. A student can enroll in many
  lectures; a lecture can have many students. Each `(student, lecture)` pair is
  unique.
- **Teaches**: Lecturer —(1:M)— Lecture. Each lecture has exactly one lecturer; a
  lecturer can teach many lectures.
- **BelongsTo**: Subject —(1:M)— Lecture. Each lecture belongs to exactly one
  subject; a subject can have many lectures.