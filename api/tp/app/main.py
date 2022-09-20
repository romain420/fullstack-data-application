# from pydantic import BaseModel, Field
# from uuid import uuid4
# from typing_extensions import Annotated
# from . import schemas, models, services
from schemas import Activity as Schema_Activity
# from models import Activity as Models_Activity
from models import BaseSQL
from services import get_activity_by_id, create_activity
from database import engine, SessionLocal
from fastapi import Depends, FastAPI, HTTPException
from datetime import datetime
from sqlalchemy.orm import Session

# BaseSQL.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI(
    title="My title",
    description="My description",
    version="0.0.1",
)


# schema of data
# from typing import Optional
# class NewActivity(BaseModel):
#     id : Annotated[str, Field(default_factory=lambda: uuid4().hex)]
#     activity_name : str
#     mean_speed : float
#     #start_date : datetime
#     description : str = None

@app.get("/")
def read_root():
    return {"Hello": "toi"}


@app.get("/date")
def get_date():
    current_date = datetime.today().strftime("%B %d, %Y")
    return current_date


# @app.post("/activities/")
# def create_activity(activity : NewActivity):
#     return {"message":f"this activity has been successfully imported {activity}"}

@app.on_event("startup")
async def startup_event():
    BaseSQL.metadata.create_all(bind=engine)


# @app.get("/base_test")
# async def base_get():
#     BaseSQL.metadata.create_all(bind=engine)


@app.get("/db_connect")
async def get_connect():
    with engine.connect() as con:
        rs = con.execute('SELECT * FROM activities')
        for i in rs:
            print(i)
    # return i


@app.post("/activities")
async def post_activities(activity: Schema_Activity, db: Session = Depends(SessionLocal)):
    db_user = get_activity_by_id(activity.id, db)
    if db_user:
        raise HTTPException(status_code=400, detail="This activity already exist")
    create_activity(db, activity)

