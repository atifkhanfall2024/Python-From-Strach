# inheritance

 #***#class Teacher():

     #def Subject(self):
      #   print("Am Teach Programming")

 #class Student(Teacher):
   # def learning(self):
      #  print("AM learning from you sir")

 #s1 = Student()

 #print(s1.Subject())
 #print(s1.learning())


class Person():
    def __init__(self , name):
        self.name = name
   
    def Display(self):
        print(f"Name is {self.name}")

class Student(Person):

    def __init__(self , name , rollno):
         
         #  calling from parent constructor 
        super().__init__(name)
        self.rollno = rollno
    def show(self):
        print(f"Your name is {self.name} and your rollnumber is {self.rollno}")


# now creating an object 

std = Student("Muhammad Atif khan" , "10")
std.Display()
std.show()