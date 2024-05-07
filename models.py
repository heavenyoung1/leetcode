from pydantic import BaseModel
from typing import Union

class User(BaseModel):
    user: str = "Пользователь"
    name: str
    age: int
    
class Feedback(BaseModel):
    name: str
    message: str

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None