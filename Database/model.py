from typing import Annotated
from fastapi import  FastAPI,Depends,HTTPException,Query
from sqlmodel import Field,Session,SQLModel,create_engine,select


app = FastAPI()
class Hero(SQLModel,table=True):
    id:int | None = Field(default=None,primary_key=True)
    name: str = Field(index=True)
    age:int | None = Field(default=None,index=True)
    secret_name:str

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
connect_args = {"check_same_thread":False}
engine = create_engine(sqlite_url,connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
def get_session():
    with Session(engine) as session:
        yield session
SessionDependency = Annotated[Session,Depends(get_session)]

@app.on_event("startup")
def on_startup():
    create_db_and_tables()
@app.post("/hero/")
def create_hero(hero:Hero,session:SessionDependency):
    session.add(hero)
    session.commit()
    session.refresh(hero)
    return  hero
@app.get("/heroes/")
def read_heroes(session:SessionDependency,offset:int = 0,limit:Annotated[int,Query(le=100)]=100)-> list[Hero]:
    heroes = session.exec(select(Hero).offset(offset).limit(limit)).all()
    # data = [hero.__dict__ for hero in heroes]
    # for hero_data in data:
    #     hero_data.pop('_sa_instance_state', None)
    #
    return heroes

@app.get("/heroes/{hero_id}")
def read_hero(hero_id: int, session: SessionDependency) -> Hero:
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    return hero
