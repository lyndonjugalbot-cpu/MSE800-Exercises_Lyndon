class StudentDetails:
    def getdetails(self):
        self.student_name = input("Enter full name: ")
        self.student_age = int(input("Enter age: "))
        self.student_address = input("Enter address: ")
        self.student_id = input("Enter student ID: ")
        return self
    
class StudentInputs:
    def get_num_students(self):
        self.num_students = int(input("How many students? "))

        students = []
        for i in range(self.num_students):
            print(f"\nStudent {i + 1} of {self.num_students}")
            students.append(StudentDetails().getdetails())

        return students

    