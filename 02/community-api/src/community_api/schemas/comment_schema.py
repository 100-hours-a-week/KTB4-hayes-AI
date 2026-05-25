# comment_schema.py

from datetime import datetime

from sqlmodel import SQLModel

# =========================================
# POST /posts/{post_id}/comments (댓글 작성)
# =========================================


# 댓글 작성 요청
class CreateCommentRequest(SQLModel):
    content: str
    author: str


# 댓글 작성 result
class CreateCommentResult(SQLModel):
    comment_id: int


# 댓글 작성 전체 응답
class CreateCommentResponse(SQLModel):
    success: bool
    status: int
    code: str
    message: str
    timestamp: datetime
    result: CreateCommentResult


# =========================================
# DELETE /comments/{comment_id} (댓글 삭제)
# =========================================


# 댓글 삭제 전체 응답
class DeleteCommentResponse(SQLModel):
    success: bool
    status: int
    code: str
    message: str
    timestamp: datetime
    result: None = None
