from fastapi import FastAPI

from src.endpoints.user.endpoint import app as user_app

app = FastAPI()


@app.get("/")
def hello():
    return {"hello": "world"}


app.mount("/user", user_app)
