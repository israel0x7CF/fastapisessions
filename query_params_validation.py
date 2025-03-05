

from fastapi import FastAPI,Query
from typing import Annotated
app = FastAPI()

@app.get("/items/")
async def read_items(q:Annotated[str | None,Query(min_length=3,max_length=6)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results["q"]= q
    return results

##Query parameter list / multiple value
@app.get("/multi/")
async def read_multiple_items(q: Annotated[list[str], Query()] = ["foo", "bar"]):
    query_items = {"q": q}
    return query_items

@app.get("/title/")
async def read_items_title(
    q: Annotated[
        str | None,
        Query(
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
        ),
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results