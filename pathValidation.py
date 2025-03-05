from fastapi import FastAPI,Path,Query
from typing import Annotated
app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(item_id:Annotated[int,Path(title="id of the item")],q:Annotated[str | None,Query(alias="item-query")]=None):
    results = {"items_id":item_id}
    if q:
        results["q"] = q
    return  results

from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/orders/{item_id}")
async def reorder(*, item_id: int = Path(title="The ID of the item to get"), q: str):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

@app.get("/path/{id}")
async def numeric_path(id:Annotated[int,Path(title="item of the product",ge=0, le=100)]):
    results = {"id":id}
    return  results