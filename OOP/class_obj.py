# object oriented programming 

class Student:

    # namespace of class
    school = 'UET Peshawar'

    

# now if we wanna to creating objects 

    def __init__(self , name , roll):
        self.name = name 
        self.roll = roll

s1 = Student("Atif khan" , "10")

print(s1.name)
print(s1.__dict__)