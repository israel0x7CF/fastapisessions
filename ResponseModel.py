from fastapi import FastAPI,Body
from typing import Annotated,Any
from pydantic import BaseModel,EmailStr


app = FastAPI()
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []
class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None
@app.post("/items/")
async def create_items(items:Annotated[Item,Body])-> Item:
    return  items

@app.post("/items1/",response_model=list[Item])
async def create_items(items:Annotated[Item,Body])-> Any:
    return [
        {"name": "Portal Gun", "price": 42.0},
        {"name": "Plumbus", "price": 32.0},
    ]
@app.post("/users/",response_model=UserOut)
async def create_items(user:Annotated[UserIn,Body])-> Any:
    return user