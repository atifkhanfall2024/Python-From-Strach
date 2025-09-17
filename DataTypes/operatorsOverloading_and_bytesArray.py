# operator overloading define how operators work for user defined classes 

fruits = ['Apple' , 'Guvava' , 'Dates' , 'Angoor']
liquids = ['Milk' , 'Shake' , 'boil Sugar']
Quantity = [1 , 2, 3]

Fruit_Chat = fruits + liquids + Quantity

print(f"your fruitchat will need at least these things :  {Fruit_Chat}")


# also we also do it like

Quantity = Quantity *3
print(f'Update Quantity is : {Quantity}')



# bytesarry used for mutable sequence of bytes useful for working with binary data

check = bytearray(b'Atif')
print(f'Check Result : {check}')

check  = check.replace(b'At' , b'Ar')
print(f'Check Result : {check}')