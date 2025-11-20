from pydantic import BaseModel
from typing import List , Optional

class Comments(BaseModel):
    id:int
    content:str
    replies:Optional[List['Comments']] = None
Comments.model_rebuild()
comment = Comments(
    id=1 ,
    content= "This is My first Comment",
    replies=[
        Comments(id=2 , content="Second Reply"),
        Comments(id=3 , content="3rd Reply" , replies=[
            
        ]),

    ]
)