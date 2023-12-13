from repository.AssignmentRepo import AssignmentRepo


class AssignmentService:
    def _init_(self, assignment_repo):
        self.__repo = AssignmentRepo()

    def get_list_assignments(self):
        return self.__repo.get_all()

    def get_list_of_assignments(self):
        results = []