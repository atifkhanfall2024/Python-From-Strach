# here we will study about function params

# Chai = input('Hello Sir  , I need a cup of Tea ?    ')
# def Make_Chai(Take_order):
#     print(f'Sir , You Have Ordered A Cup Of  {Take_order} Tea')
# Make_Chai(Chai)


# Now we will study an interesting topic of arguments and keyward arguments

# with key word we also mention wiht in name before params steric and with keyward arguments we also write double args

def Classes(*IT_classes , **Basic_classes):
    print(f' This is your IT Classes {IT_classes} and these is your Basic Classes {Basic_classes}')

Classes("LLM" , "APP DEV" , "FYP" , Ethics = 'AsmatUllah' , OperationResearch = 'Naaa')

