from fastapi import Depends, FastAPI, Header, HTTPException
from typing_extensions import Annotated

async def verify_token(x_token:Annotated[str,Header()]):
    print(f"calling verify token")
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400,detail="token header is invalid")
async def verify_key(x_key:Annotated[str,Header()]):
    print(f"calling verify key")
    if x_key != "fake-super-secret-key":
      raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key

app = FastAPI(dependencies=[Depends(verify_token),Depends(verify_key)])


@app.get("/items/")
async def read_items():
    return [{"item": "Portal Gun"}, {"item": "Plumbus"}]


@app.get("/users/")
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]