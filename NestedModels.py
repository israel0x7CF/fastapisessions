from fastapi import FastAPI,Body
from pydantic import BaseModel
from typing import Annotated
app = FastAPI()
class Image(BaseModel):
    url: str
    name: str

class ItemsBucket(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []
    locationTag:dict[str,str]
    product_image:Image

@app.post("/item/")
async def addItem(item:Annotated[ItemsBucket,Body(embed= True)]):
    return item

