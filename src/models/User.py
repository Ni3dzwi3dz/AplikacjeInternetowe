from sqlalchemy import Column, Integer, String
from src.database.connector import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password_hash = Column(String)
    permissions = Column(Integer, default=0)
