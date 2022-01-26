import unittest
from Oops_School_Project import School
from Oops_School_Project import Student

class TestSchoolStudent(unittest.TestCase):

	def test_student_init(self):
		name = 'Python'
		age = 20
		student1 = Student(name,age)
		expected_name = 'Python'
		expected_age = 15
		self.assertEqual(student1.name,expected_name,'Incorrect Name')
		self.assertEqual(student1.age,expected_age,'Incorrect Age')

	def test_student_assign_roll_number(self):
		student2 = Student('Python',20)
		roll_number1 = 15
		student2.assign_roll_number(roll_number1)
		self.assertEqual(student2.roll_number,roll_number1,'Incorrect roll number')



if __name__=='__main__':
	unittest.main()

