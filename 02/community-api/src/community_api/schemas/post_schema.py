# post_schema.py

from datetime import datetime

from sqlmodel import SQLModel

# =========================================
# GET /posts (게시글 목록 조회)
# =========================================


# 게시글 1건 조회 result
class ListPostsItem(SQLModel):
    id: int
    title: str
    author: str
    created_at: str


# 게시글 목록 조회 result
class ListPostsResult(SQLModel):
    total_count: int
    items: list[ListPostsItem]


# 게시글 목록 조회 전체 응답
class ListPostsResponse(SQLModel):
    success: bool
    status: int
    code: str
    message: str
    timestamp: datetime
    result: ListPostsResult


# =========================================
# GET /posts/{post_id} (게시글 상세 조회)
# =========================================


# 게시글 댓글 comments
class GetPostCommentItem(SQLModel):
    id: int
    content: str
    author: str


# 게시글 1건 result
class GetPostResult(SQLModel):
    id: int
    title: str
    content: str
    author: str
    created_at: str
    comments: list[GetPostCommentItem]


# 게시글 상세 조회 전체 응답
class GetPostResponse(SQLModel):
    success: bool
    status: int
    code: str
    message: str
    timestamp: datetime
    result: GetPostResult


# =========================================
# POST /posts (게시글 작성)
# =========================================


# 게시글 작성 요청
class CreatePostRequest(SQLModel):
    title: str
    content: str
    author: str


# 게시글 작성 result
class CreatePostResult(SQLModel):
    id: int


# 게시글 작성 전체 응답
class CreatePostResponse(SQLModel):
    success: bool
    status: int
    code: str
    message: str
    timestamp: datetime
    result: CreatePostResult


# =========================================
# DELETE /posts/{post_id} (게시글 삭제)
# =========================================


# 게시글 삭제 전체 응답
class DeletePostResponse(SQLModel):
    success: bool
    status: int
    code: str
    message: str
    timestamp: datetime
    result: None = None


# =========================================
# POST /posts/{post_id}/summary (게시글 요약)
# =========================================


# 게시글 요약 result
class SummarizePostResult(SQLModel):
    id: int
    summary: str


# 게시글 요약 전체 응답
class SummarizePostResponse(SQLModel):
    success: bool
    status: int
    code: str
    message: str
    timestamp: datetime
    result: SummarizePostResult


# =========================================
# POST /posts/{post_id}/comments/summary (댓글 전체 요약)
# =========================================


# 댓글 요약 result
class SummarizeCommentsResult(SQLModel):
    id: int
    summary: str


# 댓글 요약 전체 응답
class SummarizeCommentsResponse(SQLModel):
    success: bool
    status: int
    code: str
    message: str
    timestamp: datetime
    result: SummarizeCommentsResult
