from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from datetime import datetime
from typing import List, Union
from pydantic import BaseModel

# app = FastAPI()

# @app.get("/")
# async def root():
#     return FileResponse("index.html")

# @app.post("/sum")
# async def sum(request: Request):
#     num1 = await request.form['number1']
#     num2 = await request.form['number2']
#     return {'result': int(num1) + int(num2)}

# @app.get("/custom")
# async def read_custom_message():
#     return {"message":  "This is a cutom message!"}

class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: Union[datetime, None] = None
    friends: List[int] = []

#Внешние данные, имитирует входящий JSON
external_data = {
    "id": "123",
    "signup_ts": "2024-04-04 13:55",
    "friends": [1, "2", b"3"],
}
#Имитируем распаковку входящих данных в коде приложения
user = User(**external_data)
print(user)
# > User id=123 name = 'John Doe' signup_ts=datetime.datetime(2024, 4, 4, 13, 55) friends=[1, 2, 3]
print(user.id)
# > 123