# comment_controller.py

from datetime import datetime

from sqlmodel import Session

from community_api.models.comment import Comment
from community_api.models.post import Post
from community_api.schemas.comment_schema import CreateCommentRequest


def create_comment(
    session: Session, post_id: int, payload: CreateCommentRequest
) -> int | None:
    post = session.get(Post, post_id)
    if post is None:
        return None

    comment = Comment(
        post_id=post.id,
        content=payload.content,
        author=payload.author,
        created_at=datetime.now().isoformat(timespec="seconds"),
    )
    session.add(comment)
    session.commit()
    session.refresh(comment)
    return comment.id


def delete_comment(session: Session, comment_id: int) -> bool:
    comment = session.get(Comment, comment_id)
    if comment is None:
        return False

    session.delete(comment)
    session.commit()
    return True
