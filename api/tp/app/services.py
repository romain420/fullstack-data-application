from sqlalchemy.orm import Session
from fastapi import HTTPException
# from . import schemas, models
from schemas import Activity as Schemas_Activity
from models import Activity as Models_Activity


# get activity by ID to be sure we don't post the same
def get_activity_by_id(post_id: str, db: Session) -> Models_Activity:
    record = db.query(Models_Activity).filter(Models_Activity.id == post_id).first()
    if not record:
        raise HTTPException(status_code=404, detail="Not Found")
    record.id = str(record.id)
    return record


# create the activity in call in the 'main.py' to post the activity
def create_activity(db: Session, post: Schemas_Activity) -> Models_Activity:
    record = db.query(Models_Activity).filter(Models_Activity.id == post.id).first()
    if record:
        raise HTTPException(status_code=409, detail="Already exists")
    db_post = Models_Activity(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    db_post.id = str(db_post.id)
    return db_post
