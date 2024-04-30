from typing import Union
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def root_action():
    return {"surname": "Шаповалов", "name": "Александр"}

@app.get("/users")
def users_action():
    return {"phone_number": "88005553535", "email": "user1337@gmail.com"}

@app.get("/tools")
def users_action():
    return {"info": "Sample text"}