from fastapi import FastAPI,Body
from pydantic import  BaseModel,Field
from typing import Annotated


app = FastAPI()
class Item(BaseModel):
    name:str
    price:float = Field
    tax:float
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                }
            ]
        }
    }
class ExistingItem(BaseModel):
    name:str
    price:float = Field
    tax:float

@app.post("/items/")
async def add_items(items:Annotated[Item,Body(embed = True)]):
    return items
@app.post("/items/new")
async def add_existing(items:Annotated[ExistingItem,Body(embed=True,openapi_examples={
                "normal": {
                    "summary": "A normal example",
                    "description": "A **normal** item works correctly.",
                    "value": {
                        "name": "Foo",
                        "description": "A very nice Item",
                        "price": 35.4,
                        "tax": 3.2,
                    },
                },
                "converted": {
                    "summary": "An example with converted data",
                    "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
                    "value": {
                        "name": "Bar",
                        "price": "35.4",
                    },
                },
                "invalid": {
                    "summary": "Invalid data is rejected with an error",
                    "value": {
                        "name": "Baz",
                        "price": "thirty five point four",
                    },
                },
            },)]):
    return items