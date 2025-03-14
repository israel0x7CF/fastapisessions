from fastapi import FastAPI,Form
from typing import Annotated

app = FastAPI()


@app.post("/login/")
async def login(username:Annotated[str,Form()],password:Annotated[str,Form()]) -> dict:
    return {"username":username,"password":password}