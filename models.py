from pydantic import BaseModel

class User(BaseModel):
    user: str = "Пользователь"
    name: str
    age: int
    
class Feedback(BaseModel):
    name: str
    message: str