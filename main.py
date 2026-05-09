from fastapi import FastAPI
from pydantic import EmailStr
import uvicorn

# Создание приложения
app = FastAPI()

@app.get("/users")
def hello(name: str = "World"): # Значение по умолчанию
    return f"Hello {name}!"

@app.get("/users/last")
def last_user():
    return {
        "id" : {
            "user" : "name"
        }
    }

@app.post("/users/create/")
def create_email(email: EmailStr):
    return {
        "message" : "Почта добавлена",
        "email" : email
    }

@app.get("/users/{id}")
def hello_id(id: int):
    return {
        "id" : id
    }

if __name__ == "__main__":
    uvicorn.run("main:app", reload = True)