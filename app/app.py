from fastapi import FastAPI,HTTPException
from app.schemas import PostCreate

app = FastAPI()

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

@app.get("/posts")
def get_all_posts(limit: int = None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts

@app.get("/posts/{id}")
def get_post(id:int):
    if id not in text_posts:
        raise HTTPException(status_code=404,detail="Post Not Found")
    return text_posts.get(id)
    
@app.post("/posts")
def create_post(post:PostCreate):
    new_post = {"title":post.title,"content":post.content}
    text_posts[max(text_posts.keys())+1] = new_post
    return new_post