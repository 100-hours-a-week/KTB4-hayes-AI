# posts.py

from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from community_api.controllers import post_controller
from community_api.database import get_session
from community_api.schemas.post_schema import (
    CreatePostRequest,
    CreatePostResponse,
    CreatePostResult,
    DeletePostResponse,
    GetPostCommentItem,
    GetPostResponse,
    GetPostResult,
    ListPostsItem,
    ListPostsResponse,
    ListPostsResult,
)

router = APIRouter(prefix="/posts", tags=["posts"])


@router.get("", response_model=ListPostsResponse)
def read_posts(session: Session = Depends(get_session)):
    total_count, posts = post_controller.list_posts(session)

    items = [
        ListPostsItem(
            id=post.id,
            title=post.title,
            author=post.author,
            created_at=post.created_at,
        )
        for post in posts
    ]

    return ListPostsResponse(
        success=True,
        status=200,
        code="SUCCESS",
        message="게시글 목록 조회에 성공했습니다.",
        timestamp=datetime.now(),
        result=ListPostsResult(total_count=total_count, items=items),
    )


@router.get("/{post_id}", response_model=GetPostResponse)
def read_post(post_id: int, session: Session = Depends(get_session)):
    post = post_controller.get_post(session, post_id)
    if post is None:
        raise HTTPException(status_code=400, detail="잘못된 요청입니다.")

    comments = post_controller.get_post_comments(session, post_id)
    comment_items = (
        GetPostCommentItem(
            id=comment.id, content=comment.content, author=comment.author
        )
        for comment in comments
    )

    return GetPostResponse(
        success=True,
        status=200,
        code="SUCCESS",
        message="상세 조회에 성공했습니다.",
        timestamp=datetime.now(),
        result=GetPostResult(
            id=post.id,
            title=post.title,
            content=post.content,
            author=post.content,
            created_at=post.created_at,
            comments=comment_items,
        ),
    )


@router.post("", response_model=CreatePostResponse, status_code=status.HTTP_201_CREATED)
def create_post(payload: CreatePostRequest, session: Session = Depends(get_session)):
    post_id = post_controller.create_post(session, payload)

    return CreatePostResponse(
        success=True,
        status=201,
        code="CREATED",
        message="게시글 작성에 성공했습니다.",
        timestamp=datetime.now(),
        result=CreatePostResult(id=post_id),
    )


@router.delete("/{post_id}", response_model=DeletePostResponse)
def remove_post(post_id: int, session: Session = Depends(get_session)):
    deleted = post_controller.delete_post(session, post_id)
    if not deleted:
        raise HTTPException(status_code=400, detail="잘못된 요청입니다.")

    return DeletePostResponse(
        success=True,
        status=200,
        code="SUCCESS",
        message="게시글 삭제에 성공했습니다.",
        timestamp=datetime.now(),
        result=None,
    )
