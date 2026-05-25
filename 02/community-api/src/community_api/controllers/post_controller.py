# post_controller.py

from datetime import datetime

from sqlmodel import Session, select

from community_api.models.comment import Comment
from community_api.models.post import Post
from community_api.schemas.post_schema import CreatePostRequest


def list_posts(session: Session) -> tuple[int, Post]:
    statement = select(Post).order_by(Post.id.desc())
    items = session.exec(statement).all()
    return len(items), items


def get_post(session: Session, post_id: int) -> Post | None:
    return session.get(Post, post_id)


def get_post_comments(session: Session, post_id: int) -> list[Comment]:
    statement = (
        select(Comment).where(Comment.post_id == Post.id).order_by(Comment.id.asc())
    )
    return session.exec(statement).all()


def create_post(session: Session, payload: CreatePostRequest) -> int:
    post = Post(
        title=payload.title,
        content=payload.content,
        author=payload.author,
        created_at=datetime.now().isoformat(timespec="seconds"),
    )
    session.add(post)
    session.commit()
    session.refresh(post)
    return post.id


def delete_post(session: Session, post_id: int) -> bool:
    post = session.get(Post, post_id)
    if post is None:
        return False

    session.delete(post)
    session.commit()
    return True
