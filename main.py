from fastapi import FastAPI
from models import Feedback, User
import json

app = FastAPI()

fake_users = {
    1: {"username": "Homer Simpson", "email": "homer@mail.ru"},
    2: {"username": "Bart Simpson", "email": "bart@mail.ru"},
}

reviews = []
resp_ok = "Feedback received. Thank you, Alice!"
resp_no = "Feedback is shit.."

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
    if len(feed.message) > 20:
        with open("feedback.json", "w", encoding='utf-8') as file:
            pair = {feed.name : feed.message}
            json.dump(pair, file)
        return resp_ok
    return resp_no

@app.get("feedback/{name}")
def read_feed(name: str):
    with open("feedback.json", "r", encoding='utf-8') as file:
        file.load