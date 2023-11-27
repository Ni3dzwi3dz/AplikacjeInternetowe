from sqlalchemy.ext.declarative import declarative_base

from src.config.config_creator import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(config.database_config.connection_string())
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
