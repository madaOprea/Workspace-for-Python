from domain.Student import Student
from repository.StudentRepo import StudentRepo


class StudentService:
    def _init_(self):
        self.__repo = StudentRepo()
        # self.__validator = StudentValidator()

    def add(self, id, name, group):
        student = Student(id, name, group)
        # self.__validator.validate(singer)
        self.__repo.add_student(student)

    def edit(self, id, name, group):
        student = Student(id, name, group)
        self.__repo.edit_student(student)

    def get_all(self):
        return self.__repo.get_all()

    def get_students_with_grade_less_than5(self):
        bad_students = []

        for assignment in self.assignments:
            if assignment.get_grade() < 5:
                student = assignment.get_student()
                bad_students.append(student)

        return bad_students
