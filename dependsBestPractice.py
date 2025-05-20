from fastapi import FastAPI, Depends
from typing import Annotated, Optional

from fastapi.encoders import jsonable_encoder

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

class CommonQueryParams:
    def __init__(self, q: Optional[str] = None, skip: int = 0, limit: int = 10):
        self.q = q
        self.skip = skip
        self.limit = limit

async def get_filtered_items(params: CommonQueryParams = Depends()):

    items = fake_items_db[params.skip : params.skip + params.limit]
    if params.q:
        items = [item for item in items if params.q.lower() in item["item_name"].lower()]
    return items

@app.get("/items/")
async def read_items(items: Annotated[list, Depends(get_filtered_items)]):
    return {"items": items}