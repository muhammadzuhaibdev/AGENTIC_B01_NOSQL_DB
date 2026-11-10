from fastapi import APIRouter
from pydantic import BaseModel
from config.db_connection import db

postRouter = APIRouter()

postCollection = db["posts"]

class Post(BaseModel):
    title: str
    description: str
    status: str

@postRouter.post("/create")
def create_post(postData: Post):
    try:
        db_data = postCollection.insert_one(
            {
                "title": postData.title,
                "description": postData.description,
                "status": postData.status,
            }
        )

        return {
            "status": "success",
            "data": {
                "id": str(db_data.inserted_id),
                "title": postData.title,
                "description": postData.description,
                "status": postData.status,
            },
            "message": "Post Created Successfully!",
        }
    except Exception as e:
        return {
            "status": "error",
            "data": [],
            "message": str(e),
        }