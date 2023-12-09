from sqlalchemy.ext.declarative import declarative_base

from src.config.config_creator import config
from src.config.rosa_config import DatabaseConfig
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Connector:
    def __init__(self, config: DatabaseConfig):
        self.engine = create_engine(config.connection_string())
        self.session = sessionmaker(
            autocommit=False, autoflush=False, bind=self.engine
        )()

    def query(self, query: Base):
        return self.session.query(query)


connector = Connector(config.database_config)
