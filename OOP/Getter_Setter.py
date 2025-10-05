# Getter and Setter and property decorator  in python 

class Voting():

    def __init__(self , name , age):
        self._age = age
        self._name = name

    @property
   
    def age(self):
     return self._age +1
    

    @age.setter
    def age(self ,value):
       if value>= 18:
          self._age = value
          print(f" {self._name} Your Can Vote")
       else:
          raise ValueError( f" {self._name} Your are under 18 Your Cannot Vote")
        
vote = Voting("Muhammad Atif khan" , 19)

print(vote.age)
vote.age = 12
