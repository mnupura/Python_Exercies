#Part 1:
class Person():
    def __init__(self, name):
        self.name = name

    def who_am_i(self):
        print("I am Person")
        print(self.name)

    def walk(self):
        print("I can walk")

class Employee(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)
        self.__emp_id = emp_id

    def who_am_i(self):
        print("I am Employee")
        print(self.name + " : " + str(self.__emp_id))   #self._Person__name

class Manager(Employee):
    pass

p = Person("Some Person")
e = Employee("Employee one", 24)
m = Manager("Manager one",12)
print(p.who_am_i())
print(e.who_am_i())
print(e.walk())
print(m.who_am_i())
m.walk()