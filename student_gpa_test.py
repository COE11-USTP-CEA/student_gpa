import unittest
from student_gpa import Subject, Student

class Test_Student_GPA(unittest.TestCase):
    
    def setUp(self):
        self.subject = Subject('COE11', 65.10)
        self.student = Student('Juan dela Cruz', 'Male', 'CEA')

    def test_subject_get_grade(self):
        '''Test subject get_grade method'''
        self.assertEqual(self.subject.get_grade(), 65.10)
    
    def test_subject_get_name(self):
        '''Test subject get_name method'''
        self.assertEqual(self.subject.get_name(), 'COE11')

    def test_student_get_name(self):
        '''Test student get_name'''
        self.assertEqual(self.student.get_name(), 'Juan dela Cruz')

if __name__ == '__main__':
    unittest.main()