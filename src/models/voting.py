from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from src.database.connector import Base


class Voting(Base):
    __tablename__ = "votings"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    start_date = Column(DateTime)
    end_date = Column(DateTime)


class Option(Base):
    __tablename__ = "options"

    id = Column(Integer, primary_key=True, index=True)
    option = Column(String)
    voting_id = Column(Integer, ForeignKey("votings.id"))


class Vote(Base):
    __tablename__ = "votes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    voting_id = Column(Integer, ForeignKey("votings.id"))
    option_id = Column(Integer, ForeignKey("options.id"))
