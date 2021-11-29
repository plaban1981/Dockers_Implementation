from pydantic import BaseModel
from typing import Optional
from fastapi import Query

class Person(BaseModel):
    name:str
    stream:str
    roll:int
    CGPA:float


class Record(BaseModel):
    id:int
    reference:Optional[str]='No Reference' # Optional argument. By default the value will be No Reference
    fees:float
    penalty:Optional[int]=0 # Optional argument. By default the value will be 0


class University(BaseModel):
    id:int
    name:str = Query(...,max_length=10) # This means name is mandatory(...) and the max length of name can be 10
    rank:int = Query(...,ge=1) # This means rank is mandatory(...) and rank must be greater than equal to 1
