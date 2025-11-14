# now i working on adding validations with field

from pydantic import BaseModel , Field
from typing import Optional


class Employee(BaseModel):
    id:int
    name: str = Field(
        ...,
        min_length=3,
        max_length=30,
        description='Employee Name'

    )
    department: Optional[str] = 'General'

    salary:float = Field(
        ...,
        ge=10000,
        
    le=100000,
    description='Monthly Salary in USD'
    )
  

