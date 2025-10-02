# Attributes shadowing

class Student:

    name = "Muhammad Atif khan"
    location = "University Town Peshawar"

s1 = Student()

print(s1.location)

s1.name = "Ali khan"

print(s1.name)
print(Student.name)

del s1.name


print(s1.name)
print(Student.name)

