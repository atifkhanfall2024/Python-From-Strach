# here we will study about recursion 

def Recursion(n):
    if n<0:
        print('Value is Less Than Zero Must Enter Value With Zero or Greater Than ... ')
    elif n == 0 or n == 1:   
        return 1
    else:
        return n* Recursion(n-1)

Value = int(input(" Enter the value to find its factorial........ "))
a = Recursion(Value)
print(f'Factorial Of {Value} is  {a}  ')
