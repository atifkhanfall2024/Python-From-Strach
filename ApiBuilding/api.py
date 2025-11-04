from fastapi import FastAPI
from pydantic import BaseModel


class items(BaseModel):
    name:str
    price:float



app = FastAPI()


@app.get('/')
def GetData():
    return ('message : Hi this is get method')


@app.post('/items/')
def PostMethod(item:items):
    return('Product Information is :  ' , item)