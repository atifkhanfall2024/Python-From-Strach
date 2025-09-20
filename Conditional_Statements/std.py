# write a program to grade for students

Marks = int(input("Please Enter your Makrs : "))

if Marks >= 40 and Marks <=60:
    print('Your Grade is C')
elif Marks >=61 and Marks <=80:
    print("your Grade is B ")
elif Marks <=39 and Marks<0:
    print('You Are fail')
elif Marks>=81 and Marks <=100:
    print("You have Grade A")
else:
    print('please enter valid Value')