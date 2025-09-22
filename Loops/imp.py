# Break and continue statements

Colors = ['Black' , 'white' , 'yellow' , 'red' , 'pink']

for col in Colors:
    if col == "yellow":
        continue
    if col == "pink":
        print(f'differents colors  : {col}')
        break
    print(f'differents colors is : {col}')
print('you are out of loop ')