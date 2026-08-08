#import class to get the student details
from students import StudentDetails
from students import StudentInputs



#main function to get the student details and print them, sorted by age
def main():

    #get how many number of students to be inputed.
    students = StudentInputs().get_num_students()

     #sort the students by age, youngest first
    students.sort(key=StudentInputs.get_student_age, reverse=False)
   

    #print the student details, sorted by age
    print("\n" + "-" * 45)

    #print the youngest student
    print(f"{students[0].student_name} is the youngest student.")

    #print all the student details, sorted by age
    for student_details in students:
        print("-" * 45)
        print(f"Student Name: {student_details.student_name}")
        print(f"Student Age: {student_details.student_age}")
        print(f"Student Address: {student_details.student_address}")
        print(f"Student ID: {student_details.student_id}")

if __name__ == "__main__":
    main()