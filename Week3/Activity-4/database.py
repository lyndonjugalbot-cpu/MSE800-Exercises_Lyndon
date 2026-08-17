import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "school.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS Subject (
    subject_code TEXT PRIMARY KEY,
    subject_name TEXT NOT NULL,
    subject_unit INTEGER NOT NULL,
    subject_description TEXT
);
CREATE TABLE IF NOT EXISTS Lecturer (
    lecturer_id TEXT PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    address TEXT
);
CREATE TABLE IF NOT EXISTS Student (
    student_code TEXT PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    gender TEXT,
    birth_date TEXT,
    address TEXT,
    email TEXT NOT NULL UNIQUE,
    phone_number TEXT
);
CREATE TABLE IF NOT EXISTS Lecture (
    lecture_id TEXT PRIMARY KEY,
    subject_code TEXT NOT NULL REFERENCES Subject(subject_code),
    lecturer_id TEXT NOT NULL REFERENCES Lecturer(lecturer_id),
    lecture_name TEXT NOT NULL,
    room TEXT,
    day_time TEXT,
    capacity INTEGER NOT NULL
);
CREATE TABLE IF NOT EXISTS Enrollment (
    student_code TEXT NOT NULL REFERENCES Student(student_code),
    lecture_id TEXT NOT NULL REFERENCES Lecture(lecture_id),
    enrollment_date TEXT NOT NULL,
    enrollment_status TEXT NOT NULL DEFAULT 'active',
    PRIMARY KEY (student_code, lecture_id)
);
"""


class Database:
    def __init__(self, db_path=DB_PATH):
        self.db_path = str(db_path)

    def connect(self):
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA foreign_keys = ON")
        conn.row_factory = sqlite3.Row
        return conn

    def create_tables(self):
        conn = self.connect()
        conn.executescript(SCHEMA)
        conn.commit()
        conn.close()

    def is_empty(self):
        conn = self.connect()
        n = conn.execute("SELECT COUNT(*) FROM Student").fetchone()[0]
        conn.close()
        return n == 0
