from Assignment import Assignment


class AssignmentController:
    def __init__(self, studentRepository, subjectRepository):
        self.__studentRepository = studentRepository
        self.__subjectRepository = subjectRepository
        self.__assignments =[]

    def add_assignment(self, student_id, subject_id, grade):
        student = self.__studentRepository.find_by_id(student_id)
        subject = self.__subjectRepository.find_by_id(subject_id)
        
        if student and subject:
            assignment = Assignment(student, subject, grade)
            self.__assignments.append(assignment)
            return assignment
        else:
            print(f"It could not be added the new assignments")

    def update_assignment_grade(self, student_id, new_grade):
         for assignment in self.__assignments:
            if assignment.get_student().student_id == student_id:
                assignment.set_grade(new_grade)


    def delete_assignment(self, assignment):
        self.__assignments.remove(assignment)

    def get_all_assignments(self):
        return self.__assignments

    def get_list_of_assignments(self):
        results = []
        return results

    def get_students_with_grade_less_than5(self):
        bad_students = []

        for assignment in self.assignments:
            if assignment.get_grade() < 5:
                student = assignment.get_student()
                bad_students.append(student)

        return bad_students
