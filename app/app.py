from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate, PostResponse

app = FastAPI()

text_posts = {
    "1": {"title": "First Post", "content": "This is the content of the first post."},
    "2": {"title": "Second Post", "content": "This is the content of the second post."},
    "3": {"title": "Third Post", "content": "This is the content of the third post."},
    "4": {"title": "Fourth Post", "content": "This is the content of the fourth post."},
    "5": {"title": "Fifth Post", "content": "This is the content of the fifth post."},
    "6": {"title": "Sixth Post", "content": "This is the content of the sixth post."},
}

@app.get("/posts")
async def get_all_posts(limit: int = None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts

@app.get("/posts/{post_id}")
async def get_post(post_id: str):
    post = text_posts.get(post_id)
    if post:
        return post
    raise HTTPException(status_code=404, detail="Post not found")

@app.post("/posts")
async def create_post(post: PostCreate) -> PostResponse:
    new_id = str(len(text_posts) + 1)
    text_posts[new_id] = {"title": post.title, "content": post.content}
    return text_posts[new_id]