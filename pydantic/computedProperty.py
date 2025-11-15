# working with computed property

from pydantic import BaseModel , computed_field  , Field


class Chai_bill(BaseModel):
    user_id:int
    user_name:str
    chai_type :str
    number_of_cups:int = Field(ge=1)
    price_of_cup:int = Field(gt=30)

    @computed_field(return_type=int)
    
    def total_bill(self)->int:
        return self.number_of_cups * self.price_of_cup
    

make_bill = Chai_bill(
    user_id=1 ,
    user_name='Muhammad Atif khan',
    chai_type="Special Chai",
    number_of_cups=3 ,
    price_of_cup=70
)


print(make_bill.total_bill)
print(make_bill.model_dump())