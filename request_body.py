from fastapi import  FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name:str
    description:str | None = None
    price: float
    tax: float | None = None
app = FastAPI()

@app.post("/items/")
async def create_item(item:Item):
    print(item)
    return  item

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.model_dump()}