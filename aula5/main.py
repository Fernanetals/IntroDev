from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):     
    name: str  
    password: str
    bio: str | None = None

        
users = []

@app.get("/", response_class=HTMLResponse)
async def root():
    with open("Exercicios.html") as f:
        return f.read()

@app.get("/signup", response_class=HTMLResponse)
async def sign():
    with open("aula5.html") as f:
        return f.read()

@app.get("/login", response_class=HTMLResponse)
async def login():
    with open("view_aula5.html") as f:
        return f.read()

@app.post("/login")
async def login(user : User):

    u = next((u for u in users if u.name == user.name), None)

    if (u.password == user.password):
         return {"nome": u.name, "bio": u.bio}


@app.post("/users/")
async def create_user(user : User):
    users.append(user)

    return {"usuario": user.name}


@app.get("/users/")
async def get_user(index : int | None = None):
    if (index):
        return users[index]

    return users

@app.delete ("/users/")
async def delete():
    users.clear()

    return

