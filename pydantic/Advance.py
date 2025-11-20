from pydantic import BaseModel , field_validator , model_validator

class Person(BaseModel):
    first_name:str
    last_name : str

    @field_validator('first_name' , 'last_name')

    def Check(cls , v):
        if not v.istitle():
            raise ValueError('Names Must Be Capitalized')
        return v



class Email_Checking(BaseModel):
    email:str

    @field_validator('email')

    def Emial_validator(cls , v):
        return v.islower().strip()
