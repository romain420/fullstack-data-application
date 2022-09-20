from sqlalchemy import Column, String, DateTime, Float, Integer
from sqlalchemy.dialects.postgresql import UUID
from database import BaseSQL


class Activity(BaseSQL):
    __tablename__ = "activities"

    id = Column(String, primary_key=True, index=True)#Column(UUID(as_uuid=True), primary_key=True, index=True)
    activity_name = Column(String)
    mean_speed = Column(Float)
    # start_date = Column(DateTime())
    description = Column(String)