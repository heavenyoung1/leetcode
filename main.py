from fastapi import FastAPI, File, UploadFile
from models import Feedback, User, Item
import json
from typing import Annotated, Optional

app = FastAPI()

fake_users = {
    1: {"username": "Homer Simpson", "email": "homer@mail.ru"},
    2: {"username": "Bart Simpson", "email": "bart@mail.ru"},
}

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

@app.get("/users")
def read_users(limit: int = 10):
    return dict(list(fake_users.items())[:limit])


@app.get("/users/{user_id}")
def read_user(user_id: int):
    if user_id in fake_users:
        return fake_users[user_id]
    return{"error": "User not found"}

@app.post("/feedback")
def send_feed(feed: Feedback):
        with open("feedback.json", "w", encoding="utf-8") as f:
            feed_data = feed.model_dump() #метод .dict является устаревшим, вместо него использовать model_dump, здесь мы сериализуем данные чтобы загрузих и в .json
            json.dump(feed_data, f)
            return 'OK'

@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}

@app.post("/items/")
async def create(item: Item):
     return item

def get_name_with_age(name: str, age: int):
     name_with_age = name + " is this old: " + str(age)
     return name_with_age

def process_items(items: list[str]):
     for item in items:
          print(item.capitalize)

def process_items(prices: dict[str, float]):
     for item_name, item_price in prices.items():
          print(item_name)
          print(item_price)

def process_item(item: int | str):
     print(item)

def say_hi(name: Optional[str] = None):
    if name is not None:
          print(f'Hey {name}')
    else:
         print('Hello World!')

def say_hi_1(name: str | None = None):
    if name is not None:
          print(f'Hey {name}')
    else:
         print('Hello World!')

class Person:
     def __init__(self, name: str):
          self.name = name
        
def get_person_name(a_person: Person):
     return a_person.name

#Here i'm using metadata that's standart type of python libs
def say_hello(name: Annotated[str, "this is just metadata"]) -> str:
    return f"Hello {name}"