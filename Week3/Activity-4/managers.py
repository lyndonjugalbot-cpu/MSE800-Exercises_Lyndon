import sqlite3


class SubjectManager:
    def __init__(self, db):
        self.db = db

    def add(self, code, name, unit, description=None):
        connection = self.db.connect()
        connection.execute("INSERT INTO Subject VALUES (?, ?, ?, ?)", (code, name, unit, description))
        connection.commit()
        connection.close()

    def list(self):
        connection = self.db.connect()
        rows = connection.execute("SELECT * FROM Subject").fetchall()
        connection.close()
        return rows


class LecturerManager:
    def __init__(self, db):
        self.db = db

    def add(self, lecturer_id, first, last, email, address=None):
        connection = self.db.connect()
        connection.execute("INSERT INTO Lecturer VALUES (?, ?, ?, ?, ?)", (lecturer_id, first, last, email, address))
        connection.commit()
        connection.close()

    def list(self):
        connection = self.db.connect()
        rows = connection.execute("SELECT * FROM Lecturer").fetchall()
        connection.close()
        return rows


class StudentManager:
    def __init__(self, db):
        self.db = db

    def add(self, code, first, last, gender, dob, address, email, phone):
        connection = self.db.connect()
        connection.execute(
            "INSERT INTO Student VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (code, first, last, gender, dob, address, email, phone),
        )
        connection.commit()
        connection.close()

    def list(self):
        connection = self.db.connect()
        rows = connection.execute("SELECT * FROM Student").fetchall()
        connection.close()
        return rows


class LectureManager:
    def __init__(self, db):
        self.db = db

    def add(self, lecture_id, subject_code, lecturer_id, name, room, day_time, capacity):
        connection = self.db.connect()
        connection.execute(
            "INSERT INTO Lecture VALUES (?, ?, ?, ?, ?, ?, ?)",
            (lecture_id, subject_code, lecturer_id, name, room, day_time, capacity),
        )
        connection.commit()
        connection.close()

    def list(self):
        connection = self.db.connect()
        rows = connection.execute("SELECT * FROM Lecture").fetchall()
        connection.close()
        return rows


class EnrollmentManager:
    def __init__(self, db):
        self.db = db

    def enroll(self, student_code, lecture_id, date, status="active"):
        connection = self.db.connect()
        try:
            connection.execute("INSERT INTO Enrollment VALUES (?, ?, ?, ?)", (student_code, lecture_id, date, status))
            connection.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        finally:
            connection.close()

    def list(self):
        connection = self.db.connect()
        rows = connection.execute("SELECT * FROM Enrollment").fetchall()
        connection.close()
        return rows

    def students_per_course(self):
        """Q1: how many students are registered in each course (lecture)."""
        connection = self.db.connect()
        rows = connection.execute(
            """SELECT l.lecture_id, l.lecture_name, s.subject_name, COUNT(e.student_code) AS student_count
               FROM Lecture l
               JOIN Subject s ON s.subject_code = l.subject_code
               LEFT JOIN Enrollment e ON e.lecture_id = l.lecture_id
               GROUP BY l.lecture_id
               ORDER BY l.lecture_id"""
        ).fetchall()
        connection.close()
        return rows

    def students_with_multiple_courses(self):
        """Q2: students enrolled in more than one course."""
        connection = self.db.connect()
        rows = connection.execute(
            """SELECT s.student_code, s.first_name || ' ' || s.last_name AS full_name,
                      COUNT(e.lecture_id) AS course_count
               FROM Student s
               JOIN Enrollment e ON e.student_code = s.student_code
               GROUP BY s.student_code
               HAVING COUNT(e.lecture_id) > 1
               ORDER BY s.student_code"""
        ).fetchall()
        connection.close()
        return rows
