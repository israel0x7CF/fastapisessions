from typing import Annotated
from fastapi import FastAPI,Cookie

app = FastAPI()

@app.get("/items/")
async def read_items(ads_id:Annotated[str | None ,Cookie()]):
    return {"ads_id":ads_id}