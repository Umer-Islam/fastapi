from fastapi import FastAPI


app = FastAPI()


# model and table validation
class todo (SQLMODEL, table=True):
    id : int | None = Fied(default=None, primary_key=True)
    task : str = Field(index=True, max_length=56)
    is_completed : bool = Field(default=False)


@app.get("/")
def root():

    return {"testing": "😊"}
