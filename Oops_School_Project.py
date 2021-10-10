
class School():
    def __init__(self):
        self.__admission_limit = 20
        self.__students = []

    def admit_student(self,student):
        student.assign_roll_number(len(self.__students)+1)
        self.__students.append(student)

    def display_student(self):
        for stud in self.__students:
            print(stud.name)
            print(stud.age)
            print(stud.roll_number)

class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def assign_roll_number(self, roll_number):
        self.roll_number = roll_number


DES = School()
entry=0
while entry < 3:
    name = input('Enter name: ')
    age = input('Enter age: ')
    stud = Student(name, age)
    DES.admit_student(stud)
    entry+=1

DES.display_student()
