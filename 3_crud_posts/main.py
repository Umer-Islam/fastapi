from datetime import date, datetime
from random import random

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "root get route"}


posts = []


@app.get("/posts")
async def get_all_posts():
    if len(posts) <= 0:
        return "No content"
    else:
        return posts


@app.post("/posts")
async def create_post(
    author: str,
    title: str,
    content: str,
):
    newPost = {
        "id": len(posts) + 1,
        "created by": author,
        "title": title,
        "content": content,
        "date": datetime.today(),
    }
    posts.append(newPost)
    return "newPost"
