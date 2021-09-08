
from datetime import datetime
import os
from AssignmentController import AssignmentController
from SubjectRepository import SubjectRepository
from StudentRepository import StudentRepository


class Ui:

    def __init__(self):
        self.__controller = AssignmentController()
        self.__studentRepository = StudentRepository()
        self.__subjectRepository = SubjectRepository()

    def __print_menu(self):
        print(
            """
            1 - Add new student
            2 - Add new subject
            3 - Modify student
            4 - Modify subject
            5 - Delete student
            6 - Delete subject
            7 - See all students
            8 - See all subjects
            
            9 - Add new assignment (student, subject)
            10 - Examine student ( add grade)
            11 - Print students with grade less than 5
            12 - List all assignments
            
            0 - Exit
        """
        )

    def main(self):
        self.__print_menu()
        while True:
            try:
                command = input("Enter command: ")
                if command == "1":  # Add new student
                    student_id = input("Enter id: ")
                    name = input("Name: ")
                    group = input("Group: ")
                    self.__studentRepository.add_student(student_id, name, group)

                elif command == "2":  # Add new problem
                    subject_id = input("Enter subject id: ")
                    lab_no = input("Enter lab number: ")
                    description = input("Description: ")
                    deadline = input("Deadline: ")
                    self.__subjectRepository.add_subject(subject_id, lab_no, description, deadline)

                elif command == "3":  # Modify student
                    student_id = input("Which student do you want to modify? Enter id: ")
                    self.__studentRepository.edit_student(student_id)
                elif command == "4":  # Modify subject
                    subject_id = input("Which subject do you want to modify? Enter id: ")
                    self.__subjectRepository.edit_subject(subject_id)
                elif command == "5":  # Delete student
                    student_id = input("Which student do you want to delete? Enter id: ")
                    self.__studentRepository.detele_student(student_id)
                elif command == "6":  # Delete subject
                    subject_id = input("Which subject do you want to delete? Enter id: ")
                    self.__studentRepository.delete_subject(subject_id)
                elif command == "7":  # See all students
                    self.__studentRepository.get_all_students()
                elif command == "8":  # See all subject
                    self.__studentRepository.get_all_subjects()
                elif command == "9":  # Add new assignment (student, subject, grade = 0 by default)
                    student_id = input("Which student do you want to assign to a subject?")
                    self.__controller.add_assignment(student_id, subject_id, 0)
                elif command == "10":  # Examine student ( add grade)
                    student_id = input("Which student do you want to examine? Enter id: ")
                    grade = input("Insert grade from 1 to 10: ")
                    self.__controller.update_assignment_grade(student_id, grade)
                elif command == "11":  # Print students with grade less than 5
                    self.__controller.get_students_with_grade_less_than5()
                elif command == "12":
                    self.__controller.get_list_of_assignments()
                elif command == "0":
                    break
            except ValueError:
                print("Invalid value was introduced")
            except Exception as e:
                print(f"Something went wrong: {e}")

if __name__ == "__main__":
    main()