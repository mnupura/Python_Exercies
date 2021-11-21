#class Thing():
#	pass

#print(Thing)
#example=Thing()
#print(example)

#-----------------------------------------

#class Thing3():
#	def __init__(self):
#		self.__letters = 'abc'
#	def print_letters(self):
#		print(self.__letters)

#example3 = Thing3()
#example3.print_letters()

#------------------------------------------
class Thing():
    count = 0
    
    def __init__(self, name):
        Thing.count+=1
        self.name = name
        self.count = Thing.count
        
    def display(self):
        print("I am Thing ", self.name)
        print("Count ",Thing.count)
        print("Self count ",self.count)
    
    
    def display_count(cls):
        print("Total count is ", cls.count)
        
    @classmethod
    def some_class_method(cls):
        print(cls)

Thing.some_class_method()
        
t1 = Thing("T1")
print(Thing.count)
Thing.display_count(t1)
t1.display_count()
t1.some_class_method()
print(t1.name)
t1.display()
t2 = Thing("T2")
t3 = Thing("T3")
t4 = Thing("T4")
Thing.display_count(t4)
t3.display()
