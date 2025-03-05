from fastapi import  FastAPI
from typing import  Union
from enum import Enum
app = FastAPI()
class ModelName(str,Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"
@app.get("/items/{item_id}")
async def read_items(item_id:int,q:Union[str,None] = None):
    if q:
        return {"item_id":item_id,"q":q}
    return {"item_id":item_id}

## multiple path parms
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_items(user_id:int,item_id:str,q:str | None = None,short:bool =False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
          item["q"] = q
    if not short:
        item["description"] = "This is an amazing item that has a long description"

    return item