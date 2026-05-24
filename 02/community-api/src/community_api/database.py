# database.py

from sqlmodel import Session, SQLModel, create_engine

from community_api.models.Post import Post
from community_api.models.Comment import Comment


DATABASE_URL = "sqlite:///database.db"

engine = create_engine(DATABASE_URL, echo=True)


def create_db_table():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
