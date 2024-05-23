from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel

api = FastAPI()

class Owner(BaseModel):
    name: str
    address: str

class Item(BaseModel):
    itemid: int
    description: str
    owner: Optional[Owner] = None
    ratings: List[float]
    available: bool


@api.get('/')
def get_index(argument1):
    return {
        'data': argument1
    }

@api.get('/typed')
def get_typed(argument1: int):
    return {
        'data': argument1 + 1
    }

@api.get('/addition')
def get_addition(a: int, b: Optional[int]=None):
    if b:
        result = a + b
    else:
        result = a + 1
    return {
        'addition_result': result
    }

@api.post('/item')
def post_item(item: Item):
    return item