
class School():
    def __init__(self):
        self.__admission_limit = 20
        self.__students = []

    def admit_student(self,student):
        self.__students.append(student)
        print(self.__students[0].name)
        print(self.__students[0].age)

class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

DES = School()
stud1 = Student('Nupura',10)
DES.admit_student(stud1)
