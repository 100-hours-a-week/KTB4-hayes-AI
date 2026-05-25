# comments.py

from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from community_api.controllers import comment_controller
from community_api.database import get_session
from community_api.schemas.comment_schema import (
    CreateCommentRequest,
    CreateCommentResponse,
    CreateCommentResult,
    DeleteCommentResponse,
)

router = APIRouter(tags=["comments"])


@router.post(
    "/posts/{post_id}/comments",
    response_model=CreateCommentResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_comment(
    post_id: int,
    payload: CreateCommentRequest,
    session: Session = Depends(get_session),
):
    comment_id = comment_controller.create_comment(session, post_id, payload)
    if comment_id is None:
        raise HTTPException(status_code=400, detail="잘못된 요청입니다.")

    return CreateCommentResponse(
        success=True,
        status=201,
        code="CREATED",
        message="댓글 작성에 성공했습니다.",
        timestamp=datetime.now(),
        result=CreateCommentResult(comment_id=comment_id),
    )


@router.delete("/cooments/{comment_id}", response_model=DeleteCommentResponse)
def remove_comment(comment_id: int, session: Session = Depends(get_session)):
    deleted = comment_controller.delete_comment(session, comment_id)
    if not deleted:
        raise HTTPException(status_code=400, detail="잘못된 요청입니다.")

    return DeleteCommentResponse(
        success=True,
        status=200,
        code="SUCCESS",
        message="댓글 삭제에 성공했습니다.",
        timestamp=datetime.now(),
        result=None,
    )
