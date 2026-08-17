from database import Database
from managers import EnrollmentManager, LectureManager, LecturerManager, StudentManager, SubjectManager
# Manager classes above each wrap one table and expose add()/list()/report methods.


def seed(subjects, lecturers, students, lectures, enrollments):
    # Sample data used to populate an empty database on first run.
    subjects.add("SUB01", "Database Systems", 15, "Relational databases and SQL")
    subjects.add("SUB02", "Software Engineering", 15, "SDLC and design patterns")
    subjects.add("SUB03", "Data Structures & Algorithms", 20, "Core CS algorithms")

    lecturers.add("LEC01", "John", "Smith", "john.smith@uni.ac.nz", "12 Queen St, Auckland")
    lecturers.add("LEC02", "Mary", "Jones", "mary.jones@uni.ac.nz", "8 King St, Auckland")

    # 3 courses - LEC01 teaches across two different subjects
    lectures.add("LT01", "SUB01", "LEC01", "Database Systems - Lecture A", "R101", "Mon 10:00-12:00", 30)
    lectures.add("LT02", "SUB02", "LEC02", "Software Engineering - Lecture A", "R102", "Tue 10:00-12:00", 25)
    lectures.add("LT03", "SUB03", "LEC01", "Data Structures - Lecture A", "R103", "Wed 14:00-16:00", 20)

    students.add("ST001", "Alice", "Nguyen", "F", "2002-03-14", "1 Elm St", "alice.nguyen@student.ac.nz", "021000001")
    students.add("ST002", "Ben", "Carter", "M", "2001-07-22", "2 Oak St", "ben.carter@student.ac.nz", "021000002")
    students.add("ST003", "Chloe", "Davis", "F", "2002-11-05", "3 Pine St", "chloe.davis@student.ac.nz", "021000003")
    students.add("ST004", "Daniel", "Lee", "M", "2000-01-30", "4 Birch St", "daniel.lee@student.ac.nz", "021000004")
    students.add("ST005", "Emma", "Wilson", "F", "2003-05-18", "5 Cedar St", "emma.wilson@student.ac.nz", "021000005")

    # ST001, ST003, ST005 are enrolled in more than one course
    for student_code, lecture_id, date in [
        ("ST001", "LT01", "2026-02-01"), ("ST001", "LT02", "2026-02-01"),
        ("ST002", "LT01", "2026-02-02"),
        ("ST003", "LT02", "2026-02-02"), ("ST003", "LT03", "2026-02-03"),
        ("ST004", "LT03", "2026-02-03"),
        ("ST005", "LT01", "2026-02-04"), ("ST005", "LT02", "2026-02-04"), ("ST005", "LT03", "2026-02-04"),
    ]:
        enrollments.enroll(student_code, lecture_id, date)


def menu():
    # Prints the main menu options for the user to choose from.
    print("\n==== School Enrollment System ====")
    print("1. View Students")
    print("2. View Lecturers")
    print("3. View Subjects")
    print("4. View Lectures (Courses)")
    print("5. View Enrollments")
    print("6. Report: Students registered per course")
    print("7. Report: Students enrolled in more than one course")
    print("8. Exit")


def main():
    db = Database()
    db.create_tables()

    # Managers encapsulate CRUD/query logic for each entity, sharing the same db connection.
    subjects = SubjectManager(db)
    lecturers = LecturerManager(db)
    students = StudentManager(db)
    lectures = LectureManager(db)
    enrollments = EnrollmentManager(db)

    # Only seed sample data the first time the app runs against a fresh database.
    if db.is_empty():
        seed(subjects, lecturers, students, lectures, enrollments)
        print("Database was empty - sample data has been loaded.")

    # Main application loop: show the menu, read a choice, dispatch, repeat until exit.
    while True:
        menu()
        choice = input("Select an option (1-8): ").strip()
        if choice == "1":
            # List all students.
            for s in students.list():
                print(f"  {s['student_code']} | {s['first_name']} {s['last_name']} | {s['gender']} | {s['email']}")
        elif choice == "2":
            # List all lecturers.
            for l in lecturers.list():
                print(f"  {l['lecturer_id']} | {l['first_name']} {l['last_name']} | {l['email']}")
        elif choice == "3":
            # List all subjects.
            for s in subjects.list():
                print(f"  {s['subject_code']} | {s['subject_name']} | {s['subject_unit']} units")
        elif choice == "4":
            # List all lectures (courses), including subject/lecturer/capacity info.
            for l in lectures.list():
                print(f"  {l['lecture_id']} | {l['lecture_name']} | subject={l['subject_code']} "
                      f"lecturer={l['lecturer_id']} | capacity={l['capacity']}")
        elif choice == "5":
            # List all enrollments.
            for e in enrollments.list():
                print(f"  {e['student_code']} -> {e['lecture_id']} | {e['enrollment_date']} | {e['enrollment_status']}")
        elif choice == "6":
            # Report: number of students registered per course.
            for r in enrollments.students_per_course():
                print(f"  {r['lecture_id']} ({r['lecture_name']}, {r['subject_name']}): {r['student_count']} student(s)")
        elif choice == "7":
            # Report: students enrolled in more than one course.
            rows = enrollments.students_with_multiple_courses()
            if not rows:
                print("  No students are enrolled in more than one course.")
            for r in rows:
                print(f"  {r['student_code']} | {r['full_name']} | {r['course_count']} courses")
        elif choice == "8":
            # Exit the loop and end the program.
            print("Goodbye!")
            break
        else:
            # Anything outside 1-8 is not a valid menu option.
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
