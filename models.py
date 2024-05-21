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

class New_User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: datetime | None = None
    friends: list[int] = []

external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}
