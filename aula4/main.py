from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    nome: str
    idade: int


users = []

@app.get("/", response_class=HTMLResponse)
async def root():
    with open("requests.html") as f:

        return f.read()

@app.post("/users")
async def create_user(user: User):
    users.append(user)

    return user

@app.get("/users")
async def get_users(index: int | None = None):
    if index is not None:
        return users[index]

    return users

@app.delete("/users")
async def delete_users():
    users.clear()
    return {"status": "ok"}