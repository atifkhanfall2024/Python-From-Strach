file = open('filex.txt' , 'w')

try:
    file.write("Hello sir this is muhammad atif khan")
finally:
    file.close()

# other way of making file

with open('temp.txt' , 'w') as file:
    file.write("This is Temp file")
    