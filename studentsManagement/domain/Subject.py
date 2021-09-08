class Subject:
    def __init__(self, id, labNo, description, deadline):
        self.__id = id
        self.__labNo = labNo
        self.__description = description
        self.__deadline = deadline

    def get_id(self):
        return self.__id

    def get_labNo(self):
        return self.__labNo

    def get_description(self):
        return self.__description

    def get_deadline(self):
        return self.__deadline
    
    def __str__(self):
        return f"subject(id={self.__id},labNo={self.__labNo},description={self.__description},deadline={self.__deadline})"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if not isinstance(other, problem):
            return False
        return self.get_id() == other.get_id()