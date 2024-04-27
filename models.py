from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str = "Пользователь"
    age: int

    def check_adult(self):
        adult = (self.age >= 18)
        return {"name": self.name, "age":self.age,"adult": adult}
    