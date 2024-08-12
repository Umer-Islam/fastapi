from fastapi import FastAPI

app = FastAPI()
user = []

@app.get("/users")
def root():
    return "....it works😀....."


@app.post("/users")
async def create_user(users):
    user.append(users)    
    return "f hello {user}"
