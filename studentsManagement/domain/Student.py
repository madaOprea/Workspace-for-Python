from datetime import datetime
import os

class Student:
    def __init__(self, id, name, group):
        self.__id = id
        self.__name = name
        self.__group = group    

    def get_id(self):
        return self.__id

    def get___name(self):
        return self.___name

    def get_deadline(self):
        return self.__deadline
    
    def __str__(self):
        return f"problem(id={self.__id},name={self.__name},group={self.__group})"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return self.get_id() == other.get_id()