#class for getting student details
class StudentDetails:
    def getdetails(self):
        self.student_name = input("Enter full name: ")
        self.student_age = int(input("Enter age: "))
        self.student_address = input("Enter address: ")
        self.student_id = input("Enter student ID: ")
        return self

#class for getting the number of students to be inputed and storing their details in a list
class StudentInputs:
    def get_num_students(self):
        #initialize an empty list to store student details
        students = []
        self.num_students = int(input("How many students? "))
        for i in range(self.num_students):
            print(f"\nStudent {i + 1} of {self.num_students}")
            students.append(StudentDetails().getdetails())
        return students

    #returns the sort key for a student: their age
    @staticmethod
    def get_student_age(student):
        return student.student_age