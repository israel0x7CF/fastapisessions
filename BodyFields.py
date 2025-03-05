from fastapi import FastAPI,Body,Path,Query
from typing import Annotated
from pydantic import BaseModel,Field

app = FastAPI()

class Item(BaseModel):
    name:str
    description:str | None = Field(default=None,title="description of items",max_length=300)
    price:float = Field(gt=0,description="price of the item")
    availability: bool = Field(description="is the item availble in stores")

@app.post("/items/{item_id}/")
async def model_body_test(item_id:Annotated[int,Path()],item:Annotated[Item,Body(embed= True)],q:Annotated[str , Query()]):
    print(f"itemid:${item_id}")
    print(f"query:${q}")
    return  item