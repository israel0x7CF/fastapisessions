from datetime import datetime
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import  BaseModel

fake_db = {}


class Item(BaseModel):
    title: str
    timestamp: datetime
    description: str | None = None


app = FastAPI()
@app.put("/items/{id}")
def update(id:str,item:Item):
    json_compatible = jsonable_encoder(item)
    fake_db[id] = json_compatible
    return fake_db
