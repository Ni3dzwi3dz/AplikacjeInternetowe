from fastapi import FastAPI, Request

from src.config.config_creator import config
from src.endpoints.user.manager import UserManager
from src.errors.credentials import CredentialsException

app = FastAPI(
    title="Rosa user management",
    version="0.0.1",
    summary="User management tools for Rosa",
)

manager = UserManager(
    config.token_config.secret_key,
    config.token_config.algorithm,
    config.token_config.duration,
)


@app.post(
    "/login",
)
async def login(request: Request):
    username, password = manager.get_values_from_request(request)

    if user := manager.get_user(username):
        if manager.verify_password(password, user.password_hash):
            return {
                "access_token": manager.create_access_token(
                    {"user": username, "permissions": user.permissions}
                ),
                "token_type": "bearer",
            }
        else:
            raise CredentialsException("Password incorrect")

    raise CredentialsException("No such user")


@app.post("/create")
async def create(token: str):
    pass  # TODO: add this method


@app.get("/{username:str}")
async def profile(username: str):
    user = manager.get_user(username)

    if user:
        return {"username": user.username, "permission_level": user.permissions}
