# AGENTS.md

## 프로젝트 개요
- 이 프로젝트는 FastAPI를 학습하기 위한 간단한 커뮤니티 API 서버 구현 프로젝트이다.
- 기능 범위는 게시글과 댓글 API로 제한한다.
- 사용자 기능은 구현하지 않는다.
- 이후 LLM을 연결하여 게시글 또는 댓글 요약 API를 추가할 예정이다.
- 실무 수준의 복잡한 구조보다는 FastAPI, SQLModel, SQLite, API 설계 학습을 우선한다.

## 프로젝트 규칙
- 학습을 위한 프로젝트이기에 먼저 코드를 수정하지 말고 방법을 제시한다.
- 처리 과정 메시지와 응답 메시지는 모두 한국어로 작성한다.
- 사용자가 요청한 범위를 벗어난 파일은 수정하지 않는다.
- 코드를 수정할 때는 변경 이유를 간단히 설명한다.
- 한 번에 너무 많은 구조 변경을 하지 않고, 작은 단위로 나누어 진행한다.

## 기술 스택
- Python
- FastAPI
- SQLModel
- SQLite
- Uvicorn
- Pydantic

## 아키텍처 규칙
- 프로젝트 구조는 `router-controller-model` 구조를 따른다.
- `router`는 HTTP 요청/응답과 경로 정의를 담당한다.
- `controller`는 비즈니스 로직과 요청 처리 흐름을 담당한다.
- `model`은 데이터베이스 모델 정의를 담당한다.
- 요청/응답 스키마가 필요하면 별도의 `schema` 또는 `schemas` 모듈로 분리할 수 있다.
- 라우터에 비즈니스 로직을 직접 작성하지 않는다.
- 컨트롤러는 라우터와 모델 사이의 흐름을 명확히 담당한다.

## 권장 디렉터리 구조
```text
app/
  main.py
  database.py

  routers/
    posts.py
    comments.py

  controllers/
    post_controller.py
    comment_controller.py

  models/
    post.py
    comment.py

  schemas/
    post_schema.py
    comment_schema.py

docs/
  api_spec.md
```

## 기능 범위
- 게시글 기능
  - 게시글 목록 조회
  - 게시글 단건 조회
  - 게시글 생성
  - 게시글 수정
  - 게시글 삭제

- 댓글 기능
  - 특정 게시글의 댓글 목록 조회
  - 댓글 생성
  - 댓글 수정
  - 댓글 삭제

- 제외 기능
  - 회원가입
  - 로그인
  - 인증/인가
  - 사용자 프로필
  - 좋아요
  - 대댓글
  - 파일 업로드

## API 명세 관리 규칙
- API 명세서는 `docs/api_spec.md`에 작성한다.
- API를 추가하거나 변경할 때는 먼저 `docs/api_spec.md`의 명세를 기준으로 구현한다.
- API 명세서 작성과 수정은 사용자가 직접 관리할 수 있으므로, 요청받지 않은 경우 `docs/api_spec.md`를 수정하지 않는다.
- 명세에는 HTTP Method, URL, 요청 Body, 응답 Body, 상태 코드를 포함하는 것을 권장한다.

## API 설계 규칙
- API는 REST 스타일을 기본으로 한다.
- 게시글 API 예시:
  - `GET /posts`
  - `GET /posts/{post_id}`
  - `POST /posts`
  - `PUT /posts/{post_id}`
  - `DELETE /posts/{post_id}`

- 댓글 API 예시:
  - `GET /posts/{post_id}/comments`
  - `POST /posts/{post_id}/comments`
  - `PUT /comments/{comment_id}`
  - `DELETE /comments/{comment_id}`

- 응답 모델은 가능한 한 Pydantic 또는 SQLModel 기반 스키마를 사용한다.
- 에러 상황에서는 적절한 HTTP 상태 코드를 사용한다.
- 존재하지 않는 리소스는 `404 Not Found`를 사용한다.

## 데이터베이스 규칙
- 데이터베이스는 SQLite를 사용한다.
- ORM은 SQLModel을 사용한다.
- DB 연결 설정은 `app/database.py`에서 관리한다.
- 테이블 모델은 `app/models/` 아래에 작성한다.
- 초기 학습 단계에서는 Alembic 같은 마이그레이션 도구는 사용하지 않아도 된다.

## 코드 스타일
- 함수와 변수명은 명확하게 작성한다.
- 초보자가 이해할 수 있도록 지나치게 복잡한 추상화는 피한다.
- 중복 제거보다 학습 흐름을 우선할 수 있다.
- 필요한 경우에만 간단한 주석을 추가한다.
- 타입 힌트를 가능한 한 작성한다.

## LLM 기능 추가 규칙
- LLM 연동은 기본 게시글/댓글 API 구현 이후에 진행한다.
- LLM 기능은 기존 게시글/댓글 기능과 분리해서 작성한다.
- 요약 API 예시:
  - `POST /posts/{post_id}/summary`
  - `POST /comments/{comment_id}/summary`
- LLM API 키는 코드에 직접 작성하지 않고 환경 변수로 관리한다.
- LLM 응답 실패 상황을 고려해 예외 처리를 작성한다.

## 테스트 및 실행
- 서버 실행은 기본적으로 아래 명령을 사용한다.

```bash
uvicorn app.main:app --reload
```

- 기능 추가 후 가능한 경우 간단한 API 테스트 방법을 함께 제시한다.
- 테스트 코드를 추가할 경우 `tests/` 디렉터리를 사용한다.

## 작업 방식
- 먼저 현재 프로젝트 구조를 확인한다.
- 변경 전 구현 방향을 설명한다.
- 사용자가 동의하면 필요한 파일만 수정한다.
- 수정 후 변경된 내용과 실행 방법을 요약한다.
