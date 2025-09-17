# Dictionary is the collection of key values pairs 

student  = dict({
    "name":"Muhammad Atif khan",
    "age":"22",
    "location":"university town peshawar"
})

#print(f"Am the student lets check my info : {student}")


# if u wanna to add something new here 
student['profession'] = "Ai baesed Full stack web Developer"
#print(f"Am the student lets check my info : {student}")


# lets check to delete something form this 
del student["age"]
#print(f"Am the student lets check my info : {student}")


# update something 

student["profession"] = "python dev"
#print(f"Am the student lets check my info : {student}")

# check if age is present or not 
print(f"check if age is present or not ? : {"age" in student}")


# suppose i want to give all data to new var
teacher = {}
#teacher.update(student)
#teacher = student
#print(f"Check if teacher have something or not ? {teacher}")


# also we have a get method 

new_student = student.get("name" , "Not found")
print(f"Is this is found or not ? {new_student}")