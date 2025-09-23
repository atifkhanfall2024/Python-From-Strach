from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def greet():
    return {"message" : "Hello WOorld"}

@app.get('/contact')

def contact():
    return {"message":"this is my contact page"}

# post api 

class item(BaseModel):
    name:str
    price:float
    in_stock:bool


    # post api working with postman

@app.post('/items/')

async def Create_items(item:item):
    return{"message" : "items recieved " , "data " : item}

    # now working on updation of api
@app.patch('/items/update')



async def Update_items():
    return()