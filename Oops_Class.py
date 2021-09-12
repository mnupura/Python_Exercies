# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#class Person():
#   def __init__ (self,age,name):
#      self.name=name
#       self.age=age
#        self.address=None
#    def walk(self):
#        print("I can walk")

#jai=Person(36,"Jai")
#jai.walk()
#print("My name is: ",jai.name)
#---------------------------------
class Duck():
    def __init__(self,input_name):
        self.__name=input_name
    def get_name(self):
        print("Name getter")
        return self.__name
    def set_name(self,new_name):
        print("Name setter")
        self.__name=new_name
    name_property=property(get_name,set_name)

d=Duck("Daffy")
print(d.name_property)
d.name_property="New Name"
print(d.name_property)
