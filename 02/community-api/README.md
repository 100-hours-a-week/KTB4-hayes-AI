# Community API

FastAPI + SQLModel + SQLite 기반 커뮤니티 API 프로젝트입니다.  
게시글/댓글 CRUD와 로컬 LLM(Ollama) 요약 API를 구현했습니다.

## 1. 프로젝트 목표

- FastAPI 기본 구조 학습
- SQLModel 기반 DB 모델링 학습
- `router-controller-model` 구조 구현
- 로컬 LLM(Ollama) 연동

## 2. 기술 스택

- Python
- FastAPI
- SQLModel
- SQLite
- Uvicorn
- httpx (Ollama HTTP 호출)
- Ollama (로컬 모델: `gemma4:e4b`)

## 3. 프로젝트 구조

```text
community-api/
  docs/
    API_SPEC.md              # API 명세서

  src/
    community_api/
      main.py                # FastAPI 앱 시작점, router 등록
      database.py            # DB 엔진/세션/테이블 생성

      models/                # DB 테이블 모델
        post.py
        comment.py

      schemas/               # 요청/응답 스키마
        post_schema.py
        comment_schema.py

      controllers/           # 비즈니스 로직
        post_controller.py
        comment_controller.py

      routers/               # API 경로 정의
        posts.py
        comments.py

  pyproject.toml
  uv.lock
```

## 4. 시작 방법

### 4.1 저장소 클론

```bash
git clone <repo-url>
cd 02/community-api
```

### 4.2 가상환경 생성

```bash
uv venv
```

### 4.3 가상환경 활성화

```bash
source .venv/bin/activate
```

### 4.4 패키지 설치

```bash
uv sync
```

### 4.5 서버 실행

```bash
uvicorn community_api.main:app --reload
```
> Swagger: `http://127.0.0.1:8000/docs`

## 5. 데이터 구조

`Post`와 `Comment`는 분리된 테이블이며, `Comment.post_id`가 `Post.id`를 참조합니다.

### 5.1 posts 테이블

| 필드명 | 타입 | 제약 | 설명 |
| --- | --- | --- | --- |
| id | integer | PK, auto increment | 게시글 고유 ID |
| title | string | not null | 게시글 제목 |
| content | string | not null | 게시글 본문 |
| author | string | not null | 작성자 |
| created_at | string | not null | 작성 시각 |

### 5.2 comments 테이블

| 필드명 | 타입 | 제약 | 설명 |
| --- | --- | --- | --- |
| id | integer | PK, auto increment | 댓글 고유 ID |
| post_id | integer | FK(`post.id`), index, not null | 소속 게시글 ID |
| content | string | not null | 댓글 본문 |
| author | string | not null | 작성자 |
| created_at | string | not null | 작성 시각 |

## 6. API 설계 요약

상세 스펙은 `docs/API_SPEC.md`를 기준으로 합니다.

### 6.1 게시글 API

| 기능 | 메서드 | 경로 | 요청 Body | 응답(result) 요약 |
| --- | --- | --- | --- | --- |
| 게시글 목록 조회 | GET | `/posts` | 없음 | `total_count`, `items[]` |
| 게시글 상세 조회 | GET | `/posts/{post_id}` | 없음 | `id`, `title`, `content`, `author`, `created_at`, `comments[]` |
| 게시글 작성 | POST | `/posts` | `title`, `content`, `author` | `id` |
| 게시글 삭제 | DELETE | `/posts/{post_id}` | 없음 | `null` |
| 게시글 요약 | POST | `/posts/{post_id}/summary` | 없음 | `id`, `summary` |
| 댓글 전체 요약 | POST | `/posts/{post_id}/comments/summary` | 없음 | `id`, `summary` |

### 6.2 댓글 API

| 기능 | 메서드 | 경로 | 요청 Body | 응답(result) 요약 |
| --- | --- | --- | --- | --- |
| 댓글 작성 | POST | `/posts/{post_id}/comments` | `content`, `author` | `comment_id` |
| 댓글 삭제 | DELETE | `/comments/{comment_id}` | 없음 | `null` |

## 7. 공통 응답 형식

모든 주요 응답은 아래 구조를 따릅니다.

```json
{
  "success": true,
  "status": 200,
  "code": "SUCCESS",
  "message": "요청 처리 메시지",
  "timestamp": "2026-05-25T16:00:00",
  "result": {}
}
```

## 8. 로컬 LLM(Ollama) 연동

### 8.1 서버 실행

```bash
ollama serve
```

### 8.2 모델 확인

```bash
ollama list
ollama ps
```

### 8.3 모델 중지

```bash
ollama stop gemma4:e4b
```

### 8.4 기본 호출 정보

- Ollama API: `http://localhost:11434/api/generate`
- 모델명: `gemma4:e4b`
