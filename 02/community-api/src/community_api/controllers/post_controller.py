# post_controller.py
from datetime import datetime

import httpx
from sqlmodel import Session, select

from community_api.models.comment import Comment
from community_api.models.post import Post
from community_api.schemas.post_schema import CreatePostRequest

OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "gemma4:e4b"


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


def call_ollama(prompt: str) -> str:
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False,
    }

    with httpx.Client(timeout=30.0) as client:
        resp = client.post(OLLAMA_URL, json=payload)
        resp.raise_for_status()
        data = resp.json()

    return data.get("response", "").strip()


def summarize_post(session: Session, post_id: int) -> tuple[int, str] | None:
    post = session.get(Post, post_id)
    if post is None:
        return None

    prompt = (
        "게시글을 한국어로 간결하게 요약해줘\n"
        "핵심만 3문장으로 정리해줘\n\n"
        f"[제목]\n{post.title}\n\n"
        f"[본문]\n{post.content}\n"
    )

    summary = call_ollama(prompt)
    return post.id, summary


def summarize_comment(session: Session, post_id: int) -> tuple[int, str] | None:
    post = session.get(Post, post_id)
    if post is None:
        return None

    comments = session.exec(
        select(Comment).where(Comment.post_id == post_id).order_by(Comment.id.asc())
    ).all()

    if not comments:
        return post.id, "댓글이 없습니다."

    comments_text = "\n".join([f"-{comment.content}" for comment in comments])

    prompt = (
        "다음은 게시글의 댓글 전체야.\n"
        "댓글의 공통 의견, 분위기를 한국어로 간결하게 요약해줘\n\n"
        "핵심만 3문장으로 정리해줘\n\n"
        f"[게시글 제목]\n{post.title}\n\n"
        f"[게시글 본문]\n{post.content}\n"
        f"[댓글 목록]\n{comments_text}\n"
    )

    summary = call_ollama(prompt)
    return post.id, summary
