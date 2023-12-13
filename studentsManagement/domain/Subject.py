class Subject:
    def __init__(self, id, lab, description, deadline):
        self.__id = id
        self.__lab = lab
        self.__description = description
        self.__deadline = deadline

    def get_id(self):
        return self.__id

    def get_lab(self):
        return self.__lab

    def get_description(self):
        return self.__description

    def get_deadline(self):
        return self.__deadline

    def set_id(self, new_id):
        self.__id = new_id

    def set_lab(self, new_lab):
        self.__lab = new_lab

    def set_description(self, new_description):
        self.__description = new_description

    def set_deadline(self, new_deadline):
        self.__deadline = new_deadline

    def __eq__(self, other):
        return self.__id == other.__id

    def __str__(self):
        return f'Id: {self.__id}\nLaborator: {self.__lab}\nDescriere: {self.__description}\nDeadline: {self.__deadline}\n'
