from fastapi import FastAPI
from enum import Enum
app  = FastAPI()


class ModelName(str,Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get(path="/")
async def root():
    return  {"message":"hello worlds"}

@app.get("/models/{model_name}")
async def read_model(model_name:ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

@app.get(path="/items/{item_id}")
async def read_item(item_id:int):
    return {"item_id":item_id}