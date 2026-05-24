# database.py

from sqlmodel import Field, SQLModel, Session, create_engine


class Post(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    content: str
    author: str
    created_at: str


class Comment(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    post_id: int = Field(foreign_key="post.id", index=True)
    content: str
    author: str
    created_at: str


engine = create_engine("sqlite:///database.db")
