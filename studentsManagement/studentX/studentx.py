from datetime import datetime
import os

def main_menu():
    print("Welcome to StudentX")
    print("1. Add Student")
    print("2. Add Subject")
    print("3. Delete Student")
    print("4. Delete Subject")
    print("5. Modify Student")
    print("6. Modify Subject")
    print("7. Search Student")
    print("8. Search Subject")
    print("9. Exit")
    choice = input("Enter your choice: ")
    return choice

def add_student():
    # Ensure the database folder exists
    if not os.path.exists('database'):
        os.makedirs('database')

    current_time = datetime.now()
    student_id = current_time.strftime("%Y%m%d%H%M%S")
    student_name = input("Enter Student Name: ")
    student_data = f"{student_id},{student_name}\n"

    with open(os.path.join("database", "students.txt"), "a") as db:
        db.write(student_data)

    print(f"Student added successfully with ID: {student_id}")


def add_subject():
    # Ensure the database folder exists
    if not os.path.exists('database'):
        os.makedirs('database')

    # Generate a unique ID for the subject
    current_time = datetime.now()
    subject_id = current_time.strftime("%Y%m%d%H%M%S")
    subject_name = input("Enter Subject Name: ")
    subject_data = f"{subject_id},{subject_name}\n"

    # Write the subject data to the subjects.txt file
    with open(os.path.join("database", "subjects.txt"), "a") as db:
        db.write(subject_data)

    print(f"Subject added successfully with ID: {subject_id}")

def display_students():
    students = []
    try:
        with open(os.path.join("database", "students.txt"), "r") as db:
            students = db.readlines()
    except FileNotFoundError:
        print("No students found. Please add a student first.")
        return []

    for idx, student in enumerate(students):
        student_id, student_name = student.strip().split(',')
        print(f"{idx + 1}. {student_name} (ID: {student_id})")

    return students

def delete_student():
    students = display_students()
    if not students:
        return  # No students to delete

    try:
        choice = int(input("Enter the number of the student to delete: "))
        if 1 <= choice <= len(students):
            del students[choice - 1]
        else:
            print("Invalid selection.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    # Write the updated list back to the file
    with open(os.path.join("database", "students.txt"), "w") as db:
        for student in students:
            db.write(student)

    print("Student deleted successfully.")


# Functions for delete, modify, search will go here

def main():
    while True:
        choice = main_menu()
        if choice == '1':
            add_student()
        elif choice == '2':
            add_subject()
        elif choice == '3':
            delete_student()
        elif choice == '9':
            print("Exiting StudentX...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
