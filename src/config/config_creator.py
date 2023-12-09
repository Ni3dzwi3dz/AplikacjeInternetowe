from src.config.rosa_config import RosaConfig, DatabaseConfig, TokenConfig


config = RosaConfig(
    DatabaseConfig("localhost", 3306, "Rosa", "root", "HasloDoBazy"),
    TokenConfig(40, "hs256", "hello123"),
)
