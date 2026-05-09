from fastapi import APIRouter
from pydantic import *

route = APIRouter(prefix="/users") # Ко всем путям будет добавляться /users

@route.get("/")
def hello(name: str = "World"): # Значение по умолчанию
    return f"Hello {name}!"
    

# /users + /last
@route.get("/last")
def last_user():
    return {
        "id" : {
            "user" : "name"
        }
    }


# /users + /create
@route.post("/create")
def create_email(email: EmailStr):
    return {
        "message" : "Почта добавлена",
        "email" : email
    }


# etc
@route.get("/{id}")
def hello_id(id: int):
    return {
        "id" : id
    }