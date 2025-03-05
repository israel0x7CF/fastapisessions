# If you have a group of query parameters that are related, you can create a Pydantic model to declare them.
#
# This would allow you to re-use the model in multiple places and also to declare validations and metadata for all the parameters at once.

from fastapi import  FastAPI,Query,Path,Body
from pydantic import BaseModel,Field
from typing import Annotated,Literal
app = FastAPI()

class FilterParams(BaseModel):
    model_config = {'extra':"forbid"}
    limit:int = Field(100,gt=0,le=100)
    offset:int = Field(0,ge=0)
    orderBy: Literal["created_at","updated_at"] = "created_at"
    tags:list[str] =[]

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

class User(BaseModel):
    username: str
    full_name: str | None = None


@app.put("/items/{item_id}")
def read_items(filter_query:Annotated[FilterParams,Query()],item_id:Annotated[int,Path(ge=0,le=100)],item:Item,user:User,importance:Annotated[int,Body()]):
    print(f"Running DB OP {item_id}")
    return {"filter_query":filter_query,"item":item,"user":user,"imp":importance}
@app.put("/embed/{item_id}")

# Let's say you only have a single item body parameter from a Pydantic model Item.
#
# By default, FastAPI will then expect its body directly.
#
# But if you want it to expect a JSON with a key item and inside of it the model contents, as it does when you declare extra body parameters, you can use the special Body parameter embed
def read_items(user:Annotated[User,Body()],importance:Annotated[int,Body()],item_id:int):
    print(f"Running DB OP {item_id}")
    return {"user":user}
