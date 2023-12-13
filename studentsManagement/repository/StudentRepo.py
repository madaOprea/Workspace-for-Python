from domain import *
from domain.Student import Student


class StudentRepo:
    def _init_(self):
        self.__students = []

    def get_all(self):
        return self.__students

    def get_student(self, student_id):
        for st in range(len(self.__students)):
            current_student = self.__students[st]
            if current_student.get_id() == student_id:
                return st
            else:
                print("Nu s-a gasit niciun student")

    def add_student(self, student):
        id = student.get_id()
        for current_student in self.__students:
            if current_student.get_id() == id:
                raise Exception("Id deja existent")
        self.__students.append(student)
        print(f"Studentul {student.get_name()} a fost adăugat cu succes!")

    def edit_student(self, student_id, new_name, new_group):
        for student in self.get_all():
            if student.student_id == student_id:
                student.set_name(new_name)
                student.set_group(new_group)
                return student
        return None

    def delete_student(self, student_id):
        student = self.student_repository.get_by_id(student_id)
        if student:
            self.student_repository.delete(student)
            print(f"Studentul cu ID-ul {student_id} a fost șters cu succes!")
        else:
            print(f"Nu s-a găsit niciun student cu ID-ul {student_id}!")
