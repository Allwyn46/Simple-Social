from fastapi import FastAPI

app = FastAPI()

text_posts = {
    "1":{
        "title":"New post",
        "contet":"cool text post"
    }
}

@app.get("/posts")
def get_all_posts():
    return text_posts
