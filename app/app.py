from fastapi import FastAPI,HTTPException,File,UploadFile,Form,Depends
from app.schemas import PostCreate,PostResponse,text_posts
from app.db import Post, create_db_and_tables, get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager
from sqlalchemy import select
from app.imageupload import imagekit
import shutil
import os
import uuid
import tempfile

@asynccontextmanager
async def lifeSpan(app:FastAPI):
    await create_db_and_tables()
    yield

app = FastAPI(lifespan=lifeSpan)


@app.get("/feed")
async def get_posts(session:AsyncSession = Depends(get_async_session)):
    feedData = await session.execute(select(Post).order_by(Post.created_at.desc()))
    posts = [row[0] for row in feedData.all()]

    posts_data = []
    for post in posts:
        posts_data.append(
            {
                "id": str(post.id),
                "caption": post.caption,
                "url": post.url,
                "file_type": post.file_type,
                "file_name": post.file_name,
                "created_at": post.created_at
            }
        )

    return {"posts": posts_data}

@app.post("/upload")
async def upload_post(
    file:UploadFile = File(...),
    caption:str = Form(""),
    session:AsyncSession = Depends(get_async_session)
):

    temp_file_path = None

    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(file.filename)[1]) as templ_file:
            temp_file_path = templ_file.name
            shutil.copyfileobj(file.file, templ_file)
        
        upload_result = imagekit.files.upload(
            file=open(templ_file,"rb"),
            file_name=file.filename,
            use_unique_file_name=True,
            tags=["backend-upload"]
        )

        if upload_result.response.http_status_code == 200:

            post = Post(
                caption=caption,
                url=upload_result.url,
                file_type="video" if file.content_type.startswith("video/") else "image",
                file_name=upload_result.name
            )

            session.add(post)
            await session.commit()
            await session.refresh(post)
            return post
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        if temp_file_path and os.path.exists(temp_file_path):
            os.unlink(temp_file_path)
        file.file.close()
