from fastapi import FastAPI
from src.database.connector import session
from src.models.User import User
from src.utils import compare_password

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


if __name__ == "__main__":
    user = session().query(User).first()
    print(compare_password(user.password_hash, "HasloDoRoota"))
