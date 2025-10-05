# class and static methods 

class Person():
    def __init__(self , name , age):
        self.name = name
        self.age = age

    @classmethod
    def Student(cls , student_data):
       return cls(
           student_data["name"],
           student_data["age"]
       )
    
    @classmethod
    def Employee(cls , string_data):
        name , age = string_data.split("-")
        return  cls(name , age)
    


std1 = Person.Student({"name":"Muhammad Atif khan" , "age":"22"})
std2 = Person.Employee("ALikhan-22")

print(std1.__dict__)
print(std2.__dict__)