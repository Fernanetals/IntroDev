from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):     
    name: str  
    age: int
        
users = []

@app.get("/", response_class=HTMLResponse)
async def root():
    with open("Exercicios.html") as f:
        return f.read()


@app.post("/users/")
async def create_user(user : User):
    users.append(user)


@app.get("/users/")
async def get_user(index : int | None = None):
    if (index):
        return users[index]

    return users

@app.delete ("/users/")
async def delete():
    users = []

    return

