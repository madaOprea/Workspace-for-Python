from domain.Subject import Subject


class SubjectRepo:

    def _init_(self):
        self.__subjects = []

    def add_subject(self, labNo, description, deadline):
        subject = Subject(id, labNo, description, deadline)
        self.__subjects.append(subject)
        print(f"The new subject {description} was added!")

    def edit_subject(self, subject_id, new_lab_no, new_description, new_deadline):
        subject = self.subject_repository.get_by_id(subject_id)
        if subject:
            subject.lab_no = new_lab_no
            subject.description = new_description
            subject.deadline = new_deadline
            self.subject_repository.update(subject)
            print(f"The subject with id = {subject_id} was updated!")
        else:
            print(f"It could not be found the subject with id = {subject_id}!")

    def delete_subject(self, subject_id):
        subject = self.subject_repository.get_by_id(subject_id)
        if subject:
            self.subject_repository.delete(subject)
            print(f"The subject with id = {subject_id} was removed successfully!")
        else:
            print(f"It could not be found the subject with id = {subject_id}!")

    def get_subject(self, subject_id):
        subject = self.subject_repository.get_by_id(subject_id)
        if subject:
            print(
                f"The subject with id = {subject_id} is: {subject.description}, Lab No: {subject.lab_no}, Deadline: {subject.deadline}")
        else:
            print(f"It could not be found the subject with id = {subject_id}!")

    def get_all_subjects(self):
        return self.__subjects

    def _len_(self):
        return len(self.subjects)

    @staticmethod
    def find_by_id(student_id):
        if not os.path.exists('database'):
            return None

        with open(os.path.join("database", "students.txt"), "r") as db:
            students = db.readlines()

        for student in students:
            sid, sname = student.strip().split(',')
            if sid == student_id:
                return Student(sid, sname)

        return None