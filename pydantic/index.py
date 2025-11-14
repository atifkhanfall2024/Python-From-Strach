from pydantic import BaseModel


class User(BaseModel):
    name:str
    age:int
    isAlive:bool


user = User(name="Muhammad Atif khan" , age=23 , isAlive=True )

print(user)