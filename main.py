import sys
from student import (
    add_student, view_student, search_student, update_student, delete_student
)

def includes():
    print("Student Management System")
    print("Admit new Student")
    print("View the student information")
    print("Search a Student")
    print("Update if there is a new student")
    print("Delete a Student")

def add_student_record():
    print("Admit new sStudent")
    name = input("Name: ")
    course = input("Course: ")
    mobile = input("Mobile: ")
    add_student(name, course, mobile)
    print("Added successfully")

def view_student_record():
    print("List of students")
    rows = view_student()
    if not rows:
        print("Student not found")
        return
    for r in rows:
        print(f"{r[0] r{1} r{2} r{3}}")

def search_student_record():
    print("Search a Student")
    keyword = input("Enter name/course/mobile: ")
    rows = search_student(keyword)
    if not rows:
        print("Result not found!")
    for r in rows:
        print(f"{r[0] r[1] r[2] r[3]}")

def update_student_record():
    print