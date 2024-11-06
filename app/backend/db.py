from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import create_engine

engine = create_engine("sqlite:///taskmanager.db")

SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass
