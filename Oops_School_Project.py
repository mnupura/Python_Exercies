
class School():
    admission_limit = 0

    def __init__(self):
        self.__students = []

    def admit_student(self, student):
        if self.admission_limit < 3:
            self.admission_limit+=1
            student.assign_roll_number(len(self.__students)+1)
            self.__students.append(student)
            return True
        else:
            print("Admissions full. No more seats available")
            return False
                    

    def display_student(self):
        print('------------------------------------------------')
        for stud in self.__students:
            print('Student Roll Numer: '+str(stud.roll_number))
            print('Student Name: '+stud.name)
            print('Student Age: '+str(stud.age))

class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def assign_roll_number(self, roll_number):
        self.roll_number = roll_number


DES = School()
limit = True
while limit:
    name = input('Enter name: ')
    age = input('Enter age: ')
    stud = Student(name, age)
    limit=DES.admit_student(stud)

DES.display_student()
