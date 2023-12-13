class Student:
    def __init__(self, id, name, group):
        self.__id = id
        self.__name = name
        self.__group = group

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_group(self):
        return self.__group

    def set_id(self, new_id):
        self.__id = new_id

    def set_name(self, new_name):
        self.__name = new_name

    def set_group(self, new_group):
        self.__group = new_group

    def __eq__(self, other):
        return self.__id == other.__id

    def __str__(self):
        return f'Id: {self.__id}\nNume: {self.__name}\nGrup: {self.__group}\n'
