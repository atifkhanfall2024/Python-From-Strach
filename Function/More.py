# more about python take input validate it and save into data base

def Input():
    Take_value = int(input('Enter the value that you want to validate it'))
    return Take_value

def Validate():
    Validate_value = 1234
    Take_value = Input()
    #print(Take_value)
    if Validate_value != Take_value:
       print('Validation is not Success ')
       return
    else:
         print('Yes you validate Now save Data into Database')
       


def SaveData():
    print('Save your Data into Database')


def Register():
    Validate()
    SaveData()
    print('Registeration is Success')

Register()

