from fastapi import FastAPI, HTTPException
from starlette import status
from pydantic import  BaseModel
app = FastAPI()

items = {"foo": "The Foo Wrestlers"}
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()

@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": items[item_id]}

@app.post("/items/",response_model=Item,status_code=status.HTTP_201_CREATED)
async def get_items(item:Item):
    return item