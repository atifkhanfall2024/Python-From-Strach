#  is used to add counter to an iterable or string and return enumrate object 

shoes_polish = ["Black" , "Dark" , "Brown" , "Silver"]

for index , shoe in enumerate(shoes_polish , start=0):
    print(f'{index} => Currently Avalible Polish Color is : {shoe}')