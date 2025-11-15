# using validators we make custom logics

from pydantic import BaseModel , field_validator ,Field ,model_validator

class User(BaseModel):
    name:str  = Field(..., min_length=3)
    passward:str 
    confirm_passward:str

    @model_validator(passward)
    def passward_checking(cls , values):
        if values.passward !=values.confirm_passward :
            raise ValueError('Passward Doesnot Match')
        return values


