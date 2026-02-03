from fastapi import FastAPI, HTTPException

app = FastAPI()

users = []
products = []


@app.post("/users")
def create_user(name: str):
    users.append(name)
    return {"message": "User created", "users": users}


@app.get("/users")
def read_users():
    return {"users": users}


@app.put("/users/{index}")
def update_user(index: int, name: str):
    if index < 0 or index >= len(users):
        raise HTTPException(status_code=404, detail="User not found")

    users[index] = name
    return {"message": "User updated", "users": users}


@app.delete("/users/{index}")
def delete_user(index: int):
    if index < 0 or index >= len(users):
        raise HTTPException(status_code=404, detail="User not found")

    deleted = users.pop(index)
    return {"message": "User deleted", "deleted": deleted, "users": users}


# second endpoint
@app.post("/products")
def create_product(name: str):
    products.append(name)
    return {"message": "Product created", "products": products}


@app.get("/products")
def read_products():
    return {"products": products}


@app.put("/products/{index}")
def update_product(index: int, name: str):
    if index < 0 or index >= len(products):
        raise HTTPException(status_code=404, detail="Product not found")

    products[index] = name
    return {"message": "Product updated", "products": products}


@app.delete("/products/{index}")
def delete_product(index: int):
    if index < 0 or index >= len(products):
        raise HTTPException(status_code=404, detail="Product not found")

    deleted = products.pop(index)
    return {"message": "Product deleted", "deleted": deleted, "products": products}
