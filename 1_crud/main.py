import http
from http import HTTPMethod, HTTPStatus
from tkinter.constants import NONE

from fastapi import FastAPI, HTTPException

app = FastAPI()

users = [
    {"id": 1, "username": "alice", "email": "alice@example.com", "is_active": True},
    {"id": 2, "username": "bob", "email": "bob@example.com", "is_active": True},
    {
        "id": 3,
        "username": "charlie",
        "email": "charlie@example.com",
        "is_active": False,
    },
    {"id": 4, "username": "david", "email": "david@example.com", "is_active": True},
    {"id": 5, "username": "emma", "email": "emma@example.com", "is_active": True},
    {"id": 6, "username": "frank", "email": "frank@example.com", "is_active": False},
    {"id": 7, "username": "grace", "email": "grace@example.com", "is_active": True},
    {"id": 8, "username": "henry", "email": "henry@example.com", "is_active": True},
    {"id": 9, "username": "irene", "email": "irene@example.com", "is_active": False},
    {"id": 10, "username": "jack", "email": "jack@example.com", "is_active": True},
]


@app.get("/")
async def get_user():
    return {"message": users}


@app.get("/id")
async def get_user_by_id(user_id: int):
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        raise HTTPException(
            status_code=404, detail="user is not in the list of all users"
        )
    return user


@app.get("/user")
async def get_user_by_name(user_name: str):
    user = next((u for u in users if u["username"] == user_name))
    if not user:
        raise HTTPException(status_code=404, detail="username not found")
    return user


@app.post("/")
async def add_user(username, email, is_active=True):
    next_id = max(user["id"] for user in users) + 1 if users else 1

    new_user = {
        "id": next_id,
        "username": username,
        "email": email,
        "is_active": is_active,
    }

    users.append(new_user)
    return new_user
