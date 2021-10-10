
class School():
    def __init__(self):
        self.__admission_limit = 0

    def admission_limit_reached (self):
        if admission_limit > 50:
            return "Admission full. No more seats available"

class Student():
    def __init__(self, name, age, roll_number):
        self.name = name
        self.age = age
        self.roll_number = roll_number

    def student_details_entry(self):
        self.__student_detail[int(self.roll_number)]=self.name
        self.__age_list.append(self.age)
        print(self.__student_detail)
        print("Age: " + str(self.__age_list))

entries = 0
while entries <2:
    name = input("Enter name: ")
    age = input("Enter age: ")
    roll = input("Enter roll number: ")
    stud1 = Student(name,age,roll)
    stud1.student_details_entry()
    entries+=1
