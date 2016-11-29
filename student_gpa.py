class Subject(object):
    name = ''
    grade = 0

    def __init__(self, sub_name, sub_grade):
        self.name = sub_name
        self.grade = sub_grade

    def get_name(self):
        return self.name

    def get_grade(self):
        return self.grade

class Student(object):
    subject_load = []

    def __init__(self, stud_name, stud_gender, stud_dept):
        self.name = stud_name
        self.gender = stud_gender
        self.dept = stud_dept

    def get_name(self):
        return self.name

    def add_load(self, subject):
        self.subject_load.append(subject)

    def compute_gpa(self):
        gpa = 0
        for subject in self.subject_load:
            gpa = gpa + subject.get_grade()

        return gpa / len(self.compute_gpa)

def student_gpa_main():
    # our main method this is where the business happens
    pass

if __name__ == '__main__':
    student_gpa_main()

