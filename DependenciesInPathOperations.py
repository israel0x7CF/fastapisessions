from typing import Annotated
from fastapi import Depends,FastAPI,Header,HTTPException


app = FastAPI()


async def verify_token(x_token:Annotated[str,Header()]):
    print(f"calling verify token")
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400,detail="token header is invalid")
async def verify_key(x_key:Annotated[str,Header()]):
    print(f"calling verify key")
    if x_key != "fake-super-secret-key":
      raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key
async def custom_dep(name:str):
    print("calling custom deps")

@app.get("/items/", dependencies=[Depends(verify_token), Depends(verify_key)])
async def read_items(name:Annotated[str,Depends(custom_dep)]):
    return [{"item": "Foo"}, {"item": "Bar"}]