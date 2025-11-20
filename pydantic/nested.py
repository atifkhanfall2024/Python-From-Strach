from pydantic import BaseModel
from typing import Optional , List


class Address(BaseModel):
    street:str
    city:str
    postal_code:str

class User(BaseModel):
    id:str
    name:str
    address:Address

userinfo = {
    "id":"1",
    "name":"Muhammad Atif khan",
    "address":{
        "street":"201",
        "city":"peshawar",
        "postal_code":"20001"
    }
}

user=  User(**userinfo)

print(user)