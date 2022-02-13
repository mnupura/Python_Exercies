import unittest
from Oops_School_Project import School
from Oops_School_Project import Student

# Always one test class should have responsibility of testing on model class.
#So TestSchoolStudent is wrong.
# Separate TestSchool and TestStudent class are correct.
'''
class TestStudent(unittest.TestCase):

	def test_init_should_set_name_and_age(self):
		name = 'Python'
		age = 20
		student1 = Student(name,age)
		expected_name = 'Python'
		expected_age = 15
		self.assertEqual(student1.name,expected_name,'Incorrect Name')
		self.assertEqual(student1.age,expected_age,'Incorrect Age')
		self.assertEqual(student1.roll_number,0,'Incorrect roll number')
	
	def test_assign_roll_numnber_should_update_roll_number(self):
		student1 = Student('Python',200)
		self.assertEqual(student1.roll_number,0,'rollnumber should be 0 in init')
		roll_number = 50000
		student.assign_roll_number(roll_number)
		self.assertEqual(student1.roll_number,roll_number,'Updated rollnumber should be 50000')


class TestSchool(unittest.TestCase):
	def test_school_init_instantiates_empty_students_list(self):
		des_school = School()
		self.assertEqual(len(des_school.students), 0)

	def test_is_admission_available_should_return_True_when_no_students_admitted(self):
		school = School()
		self.assertTrue(school.is_admission_available())

	def test_is_admission_available_should_return_False_when_admission_limit_reached(self):
		school = School()
		school.admit_student(1)
		school.admit_student(2)
		school.admit_student(3)
		self.assertFalse(school.is_admission_available())
	
	def test_admit_student_should_add_student_to_school_return_True(self):
		school = School()
		one = Student('one', 12)
		admission_done = school.admit_student(one)
		self.assertEqual(len(school.students), 1)
		self.assertTrue(admission_done)

	def test_admit_student_should_return_error_message_when_admission_full(self):
		school = School()
		one = Student('one', 12)
		school.admit_student(one)
		school.admit_student(one)
		school.admit_student(one)
		admission_done = school.admit_student(one)
		self.assertEqual(len(school.students), School.ADMISSION_LIMIT)
		self.assertEqual(admission_done,"Admissions full. No more seats available")

'''

#class Test_Student(unittest.TestCase):

#	def test_student_init(self):
#		name = 'Python'
#		age = 20
#		student1 = Student(name,age)
#		expected_name = 'Python'
#		expected_age = 15
#		self.assertEqual(student1.name,expected_name,'Incorrect Name')
#		self.assertEqual(student1.age,expected_age,'Incorrect Age')
#		self.assertEqual(student1.roll_number,0,'Incorrect roll number')

#	def test_student_assign_roll_number(self):
#		student2 = Student('Python',20)
#		roll_number1 = 15
#		student2.assign_roll_number(roll_number1)
#		self.assertEqual(student2.roll_number,roll_number1,'Incorrect roll number')

class Test_School(unittest.TestCase):

	def test_admit_student_admission_available(self):
		student1=Student('Stud1',1)
		school1 = School()
		admission_done = school1.admit_student(student1)
		self.assertTrue(admission_done)

	def test_is_admission_available_return_True_when_no_students_admitted(self):
		school = School()
		self.assertTrue(school.is_admission_available())

	def test_admit_student_admission_full(self):
		school2 = School()
		student2=Student('Stud2',2)
		admission_status = school2.admit_student(student2)
		self.assertTrue(admission_status)	
		student3=Student('Stud3',3)
		admission_status = school2.admit_student(student3)
		self.assertTrue(admission_status)
		student4=Student('Stud4',4)
		admission_status = school2.admit_student(student4)
		self.assertTrue(admission_status)
		student5=Student('Stud5',5)
		admission_status = school2.admit_student(student5)
		self.assertTrue(admission_status)
		
	def test_calculate_score(self):
		school = School()
		student1=Student('Stud1',40)
		admission_status = school.admit_student(student1)
		student2=Student('Stud2',50)
		admission_status = school.admit_student(student2)
		student3=Student('Stud3',60)
		admission_status = school.admit_student(student3)
		school.calculate_score()
		school.display_result()

		

if __name__=='__main__':
	unittest.main()

