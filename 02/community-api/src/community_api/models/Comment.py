# Comment.py

from sqlmodel import Field, SQLModel


class Comment(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    post_id: int = Field(foreign_key="post.id", index=True)
    content: str
    author: str
    created_at: str
