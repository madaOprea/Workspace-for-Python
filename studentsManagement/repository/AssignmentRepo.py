class AssignmentRepo:
    def _init_(self):
        self.__elements = []

    def add(self, element):

        self.__elements.append(element)

    def get_all(self):
        return self.__elements

    def _len_(self):
        return len(self.__elements)
