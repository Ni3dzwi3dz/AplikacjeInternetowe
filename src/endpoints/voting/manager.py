from src.database.connector import connector
from src.models.voting import Voting


class VotingManager:
    def __init__(self, secret_key: str, algorithm: str, expiration: int) -> None:
        self._SECRET_KEY = (
            secret_key  # TODO: refactor it, to use config class instead of algorithms
        )
        self._ALGORITHM = algorithm
        self._EXPIRATION = expiration

    async def get_user_data(self, token: str):
        pass

    async def get_current_votings(self):
        results = connector.query(Voting)
        return results
