from Student import Student


class StudentRepository:

    def __init__(self):
        self.__students = []

    def add_student(self, id, name, group):
        student = Student(id, name, group)
        self.students.append(student)
        print(f"Studentul {name} a fost adăugat cu succes!")

    def edit_student(self, student_id, new_name, new_group):
        student = self.student_repository.get_by_id(student_id)
        if student:
            student.name = new_name
            student.group = new_group
            self.student_repository.update(student)
            print(f"Studentul cu ID-ul {student_id} a fost actualizat cu succes!")
        else:
            print(f"Nu s-a găsit niciun student cu ID-ul {student_id}!")

    def delete_student(self, student_id):
        student = self.student_repository.get_by_id(student_id)
        if student:
            self.student_repository.delete(student)
            print(f"Studentul cu ID-ul {student_id} a fost șters cu succes!")
        else:
            print(f"Nu s-a găsit niciun student cu ID-ul {student_id}!")

    def get_student(self, student_id):
        student = self.student_repository.get_by_id(student_id)
        if student:
            print(f"Studentul cu ID-ul {student_id} este: {student.name}, Grupa: {student.group}")
        else:
            print(f"Nu s-a găsit niciun student cu ID-ul {student_id}!")

    def get_all_students(self):
        return self.__students

    def __len__(self):
        return len(self.__students)
    
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
