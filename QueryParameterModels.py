# If you have a group of query parameters that are related, you can create a Pydantic model to declare them.
#
# This would allow you to re-use the model in multiple places and also to declare validations and metadata for all the parameters at once.

from fastapi import  FastAPI,Query
from pydantic import BaseModel,Field
from typing import Annotated,Literal
app = FastAPI()

class FilterParams(BaseModel):
    model_config = {'extra':"forbid"}
    limit:int = Field(100,gt=0,le=100)
    offset:int = Field(0,ge=0)
    orderBy: Literal["created_at","updated_at"] = "created_at"
    tags:list[str] =[]

@app.get("/items/")
def read_items(filter_query:Annotated[FilterParams,Query()]):
    return filter_query