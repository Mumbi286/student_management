from database import Database
from student import Student

def list():
    print("STUDENT MANAGEMENT SYSTEM")
    print("Admit a student")
    print("View a student")
    print("Update Student")
    print("Delete Student")
    print("Exist")

def main():
    # Intialise database and table
    Database.initialise()

    while True:
        menu()
        choice = input("Enter choice: ").strip()

        if choice == "1": #Adds a student
            try:
                s = Student()
                s.set_name(input("Name: "))
                s.set_course(input("Course: "))
                s.set_mobile(input("Mobile: "))
                s.save()
                print("Added Successfully!")
            except ValueError as ve:
                print(f"Invalid Input: {ve}")
            except RuntimeError as re:
                print(f"Error: {re}")

        elif choice == "2": #View Students
            try:
                rows = Student.get_all()
                if not rows:
                    if not rows:
                        print("Invalid!")
                else: 
                    print("ID | Name | Course | Mobile")
                    print("-"*30)
                    for r in rows:
                    print(f"{r[0]} | {r[1]} | {r[2]} |{r[3]}")
            except RuntimeError as re:
                print(f"Error: {re}")
        
        elif choice == "3": #Update Student 
            try:
                student_id = input("Student Updated: ")
                name = input("New name: ")
                course = input("New course: ")
                mobile = input("New mobile: ")
                Student.update(student_id, name, course, mobile)
                print("Update Successful!")
            except ValueError as ve:
                 print(f"Invalid Input: {ve}")
                 except RuntimeError as re:
                print(f"Error: {re}")

        elif choice == "4": #Delete Student
           try:
                student_id = input("Student Updated: ")
                confirm = input("Are you sure ? (y/n):").strip().lower()
                if confirm == "y":
                    Student.delete(student_id)
                    print("Deleted successful!")
                else:
                    print("Cancelled")
            except ValueError as ve:
                 print(f"Invalid Input: {ve}")
                 except RuntimeError as re:
                print(f"Error: {re}")

            


            
            