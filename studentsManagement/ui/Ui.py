class UI:

    def _init_(self):
        self.studentService = StudentService()
        self.subjectRepository = SubjectRepo()
        # self.__service = AssignmentService()

    def run(self):
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

        while True:
            try:
                command = input("Enter command: ")
                if command == "1":  # Add new student
                    student_id = input("Enter id: ")
                    name = input("Name: ")
                    group = input("Group: ")
                    self.studentService.add(student_id, name, group)

                elif command == "2":  # Add new problem
                    subject_id = input("Enter subject id: ")
                    lab_no = input("Enter lab number: ")
                    description = input("Description: ")
                    deadline = input("Deadline: ")
                    self.subjectRepository.add_subject(subject_id, lab_no, description, deadline)

                # ... (rest of your code)

            except ValueError:
                print("Invalid value was introduced")
            except Exception as e:
                print(f"Something went wrong: {e}")


if __name__ == "__main__":
    app = UI()
    app.run()