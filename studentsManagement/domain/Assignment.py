from repository import *
from domain import *

class Assignment:
    def __init__(self, student: StudentRepository, subject: Subject, grade):
        self.__student = student()
        self.__subject = subject()
        self.__grade = grade

    def get_student(self):
        return self.__student

    def set_student(self, student):
        self.__student = student

    def get_subject(self):
        return self.__subject

    def set_subject(self, subject):
        self.__subject = subject

    def get_grade(self):
        return self.__grade

    def set_grade(self, grade):
        self.__grade = grade

    def __str__(self):
        return f"assignment(s={self.__student}, p={self.__subject})"

    def __repr__(self):
        return str(self)
