from fastapi import FastAPI
from sqlmodel import Field, Session, SQLModel, create_engine

import settings

app = FastAPI()


class Todo(SQLModel, table=True):
    id: int | None = Field(
        default=None, primary_key=True
    )  # user must eithre enther it themselves or they haven't entered it and db will automatically enter it, it is also called union
    content: str = Field(
        index=True, min_length=3, max_length=128
    )  # index just helps with search, not necessary for now
    is_complete: bool = Field(default=False)


conn_string: str = str(settings.DB_URL).replace("postgresql", "postgresql+psycopg")
engine = create_engine(conn_string, pool_recycle=300)
SQLModel.metadata.create_all(engine)

todo1: Todo = Todo(content="first todo task", is_complete=True)
# sessions for every transaction

session = Session(engine)

# create todos in db
# session.add(todo1)
session.commit()
print(todo1)


@app.get("/")
def root():
    return "hello world"
