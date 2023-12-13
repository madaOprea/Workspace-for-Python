from domain import Student, Subject


class Assignment:
    def __init__(self, id, student: Student, subject: Subject, grade):
        self.__id = id
        self.__student = student
        self.__subject = subject
        self.__grade = grade

    def get_id(self):
        return self.__id

    def get_student(self):
        return self.__student

    def get_subject(self):
        return self.__subject

    def get_grade(self):
        return self.__grade

    def set_id(self, id):
        self.__id = id

    def set_student(self, student):
        self.__student = student

    def set_subject(self, subject):
        self.__subject = subject

    def set_grade(self, grade):
        self.__grade = grade

    def __eq__(self, other):
        return self.__id == other.__id

    def __str__(self):
        return f'Id: {self.__id}\nStudent: {self.__student}\nLaborator: {self.__subject}\nNota: {self.__grade}\n'
