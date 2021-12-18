
class School():
    ADMISSION_LIMIT = 3
    result={}

    def __init__(self):
        self.students = []

    def admit_student(self, student):
        if len(self.students) < School.ADMISSION_LIMIT:
            student.assign_roll_number(len(self.students)+1)
            self.students.append(student)
            return True
        else:
            print("Admissions full. No more seats available")
            return False
                    
    def is_admission_available(self):
        return (len(self.students) < School.ADMISSION_LIMIT)

    def display_student(self):
        print('------------------------------------------------')
        for stud in self.students:
            print('Student Roll Number: '+str(stud.roll_number))
            print('Student Name: '+stud.name)
            print('Student Age: '+str(stud.age))

    def calculate_score(self):
        score = 0
        roll = 0
        for stud in self.students:
            roll = stud.roll_number
            score = ((roll + 50)/(len(self.students)))
            School.result[roll] = [stud.name,score]

    def display_result(self):
        print('------------------------------------------------')
        print('Roll Number'+ '  |  '+'Student Name'+'  |  '+'Score')
        for x,y in School.result.items():
            print(str(x) + '            |  '+str(y[0])+'            |  '+str(y[1]))
        

class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.roll_number = 0

    def assign_roll_number(self, roll_number):
        self.roll_number = roll_number

    
DES = School()

while DES.is_admission_available():
    name = input('Enter name: ')
    age = input('Enter age: ')
    stud = Student(name, age)
    DES.admit_student(stud)


DES.display_student()
DES.calculate_score()
DES.display_result()

