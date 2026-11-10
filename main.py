from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()
from routes.student_routes import studentRouter
from routes.post_routes import postRouter

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # restrict to your frontend's origin in production
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(studentRouter, prefix="/student", tags=["Student Management"])
app.include_router(postRouter, prefix="/post", tags=["Post Management"])


@app.get("/")
def server_testing():
    return {"msg": "Server is up & running"}
