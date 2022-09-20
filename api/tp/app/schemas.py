from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from uuid import uuid4
from typing_extensions import Annotated


class Activity(BaseModel):
    id : str#Annotated[str, Field(default_factory=lambda: uuid4().hex)]
    activity_name : str
    mean_speed : float
    # start_date : datetime
    description : str

    class Config:
        orm_mode = True