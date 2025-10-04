## Constructor is a method which is used to automatically called when its object is created 
## its used for creating an object attributes of variable 

class Student:
    def __init__(self , name , age):
        self.name = name
        self.age = age
    
    def Information(self):
        return f"My name is {self.name} and age is {self.age}"

s1 = Student("Muhammad Atif khan" , 22)

print(s1.Information())

