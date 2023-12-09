from datetime import datetime, timedelta
from jose import JWTError, jwt
from typing import Optional, Tuple

from fastapi import Request
from passlib.context import CryptContext

from src.database.connector import connector
from src.errors.credentials import CredentialsException
from src.models.user import User


class UserManager:
    context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def __init__(self, secret_key: str, algorithm: str, expiration: int) -> None:
        self._SECRET_KEY = (
            secret_key  # TODO: refactor it, to use config class instead of algorithms
        )
        self._ALGORITHM = algorithm
        self._EXPIRATION = expiration

    @staticmethod
    async def get_values_from_request(
        request: Request,
    ) -> (Optional[str], Optional[str]):
        json_payload = await request.json()

        username = json_payload.get("username", None)
        password = json_payload.get("password", None)

        if username and password:
            return username, password

        return None, None

    @staticmethod
    def get_user(username: str) -> Optional[User]:
        return connector.query(User).filter_by(username=username).first()

    def create_password_hash(self, password: str) -> str:
        return self.context.hash(password)

    def verify_password(self, password: str, hashed: str) -> bool:
        return self.context.verify(password, hashed)

    def create_access_token(self, data: dict) -> str:
        to_encode = data.copy()
        to_encode.update(
            {"exp": datetime.utcnow() + timedelta(seconds=self._EXPIRATION)}
        )

        return jwt.encode(to_encode, self._SECRET_KEY, algorithm=self._ALGORITHM)

    def get_user_data_from_token(self, token: str) -> Tuple[str, str]:
        try:
            payload = jwt.decode(token, self._SECRET_KEY, algorithms=[self._ALGORITHM])
            if "user" and "permissions" in payload.keys():
                username = payload["user"]
                permissions = payload["permissions"]
                return username, permissions

        except JWTError:
            raise CredentialsException("Could not encode token")
