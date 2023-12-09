import pytest
import unittest

from fastapi import Request
from jose import jwt

from src.endpoints.user.manager import UserManager


# TODO: unify ' and "
class TestLogin:
    manager = UserManager("secret", "HS256", 30)

    @pytest.mark.asyncio
    @unittest.mock.patch("src.endpoints.user.manager.Request.json")
    async def test_get_from_payload(self, mock_values):
        mock_values.return_value = {"username": "Krzysio123", "password": "dupa1234"}
        result = await self.manager.get_values_from_request(Request({"type": "http"}))

        assert len(result) == 2
        assert result[0] == "Krzysio123"

    def test_verify_password(self):
        password = "example_password"
        hashed = self.manager.create_password_hash(password)

        assert self.manager.verify_password(password, hashed)

    def test_create_token(self):
        token = self.manager.create_access_token({"user": "example_user", "foo": "bar"})
        encoded = jwt.decode(token, "secret", "HS256")

        assert encoded["user"] == "example_user"
        assert encoded["foo"] == "bar"
