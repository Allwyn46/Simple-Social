from pydantic import BaseModel
from fastapi_users import schemas
import uuid

text_posts = {
    1: {
        "title": "New post",
        "contet": "cool text post"
    },
    2: {
        "title": "Learning FastAPI",
        "contet": "Finally got uvicorn running without errors!"
    },
    3: {
        "title": "Random thought",
        "contet": "Coffee tastes better when the code compiles"
    },
    4: {
        "title": "Weekend plans",
        "contet": "Thinking about refactoring my whole project this weekend"
    },
    5: {
        "title": "Bug fixed!",
        "contet": "Spent 3 hours on a typo. Classic."
    },
    6: {
        "title": "Reading list",
        "contet": "Started a new book on system design"
    },
    7: {
        "title": "Late night coding",
        "contet": "Nothing beats a productive 2am debugging session"
    },
    8: {
        "title": "Music recommendation",
        "contet": "Lo-fi beats are the best coding companion"
    },
    9: {
        "title": "Gym update",
        "contet": "Finally hit a new PR today"
    },
    10: {
        "title": "Project milestone",
        "contet": "Simple_social backend is finally taking shape"
    }
}

class PostCreate(BaseModel):
    title:str
    content:str

class PostResponse(BaseModel):
    title:str
    content:str

class PostDataResponse(BaseModel):
    title:str
    content:str
    id:int
     
class UserRead(schemas.BaseUser[uuid.UUID]):
    pass

class UserCreate(schemas.BaseUserCreate[uuid.UUID]):
    pass

class UserUpdate(schemas.BaseUserUpdate[uuid.UUID]):
    pass