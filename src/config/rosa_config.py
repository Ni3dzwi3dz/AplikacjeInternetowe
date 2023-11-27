from dataclasses import dataclass


@dataclass
class DatabaseConfig:
    host: str
    port: int
    database: str
    username: str
    password: str

    def connection_string(self):
        return f"mysql://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"


@dataclass
class TokenConfig:
    duration: int  # token duration in seconds


@dataclass
class RosaConfig:
    database_config: DatabaseConfig
    token_config: TokenConfig
