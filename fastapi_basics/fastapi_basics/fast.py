from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def  home():
	return {"whatever🦉"}


@app.get("/whatever")
def whatever():
	return{"testing":"whatever endpoint"}

inventory = {
	1:{
	"name":"book",
	"catagory":"publications",
	"price": 1.34
	}
}

@app.get("/item_get/{item_id}")
def item_get(item_id:int):
	return inventory[1]

#query parameterhow to do a query parameter:


@app.get("/getByWhatever")
def getByWhatever(name:str):
	for itemId in inventory:
		if inventory[itemId]["name"] == name:
			return {inventory[itemId]["price"]}
	return {"DataNotFound😢"}