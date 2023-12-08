from typing import Union,Optional
from pydantic import BaseModel, Field
from beanie import Document, PydanticObjectId


class CustomerSignUp(Document):
    name:str=Field(min_length=5)
    email:str
    password:str
    nickname:Optional[str]=None
    
    

class CustomerLogin(Document):
    email:str
    password:str
    
class CustomerLoginRead(CustomerLogin):
     id: PydanticObjectId = Field()
     token:str

    