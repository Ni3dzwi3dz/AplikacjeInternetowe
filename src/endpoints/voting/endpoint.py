from typing import Annotated, Tuple

from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer

from src.config.config_creator import config
from src.endpoints.user.endpoint import manager as user_manager
from src.endpoints.voting.manager import VotingManager

app = FastAPI(title="Rosa voting", version="0.0.1", summary="Rosa voting management")

manager = VotingManager(
    config.token_config.secret_key,
    config.token_config.algorithm,
    config.token_config.duration,
)

reusable_oauth = OAuth2PasswordBearer(tokenUrl="/login", scheme_name="JWT")


@app.post("create")
async def create(
    user: Annotated[Tuple, Depends(user_manager.get_user_data_from_token)]
):
    pass


@app.get("current")
async def get_current():
    pass


@app.post("vote")
async def vote():
    pass
