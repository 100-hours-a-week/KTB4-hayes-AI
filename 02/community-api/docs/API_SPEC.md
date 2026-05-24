# API 명세서

# 게시글 목록 조회

카테고리: 게시글
설명: page와 size를 사용하여 게시글 목록을 조회합니다.
Method: GET
URL: /posts
param: page, size
사용자: 유저

### Request

| key | 설명 | value 타입 | 옵션 | Nullable | 예시 |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |
|  |  |  |  |  |  |

**Query parameter**

`/posts?page=1&size=10`

1. page
2. size

### Response

| key | 설명 | value 타입 | 옵션 | Nullable | 예시 |
| --- | --- | --- | --- | --- | --- |
| result.total_count | 전체 게시글 개수 | integer |  | not null | 150 |
| result.page | 현재 페이지 | integer |  | not null | 1 |
| result.items | 게시글 데이터 리스트 | array |  | not null | [{ … }] |
| result.items[].id | 게시글 고유 ID | integer |  | not null | 45 |
| result.items[].title | 게시글 제목 | string |  | not null | “첫 번째 게시글입니다.” |
| result.items[].author | 작성자 | string |  | not null | “user1” |
| result.items[].created_at | 작성 날짜 및 시간 | string |  | not null | “2026-05-23T15:00:00” |

**Example**

```json
{
	"success": true,
	"status": 200,
	"code": "SUCCESS",
	"message": "게시글 목록 조회에 성공했습니다.",
	"timestamp": "2026-05-23T17:00:00",
	"result": {
		"total_count": 100,
		"page": 1,
		"items": [
			{
				"id": 45,
				"title": "첫 번째 게시글입니다.",
				"author": "user1",
				"created_at": "2026-05-23T15:00:00"
			},
			{
				"id": 44,
				"title": "두 번째 게시글입니다.",
				"author": "user2",
				"created_at": "2026-05-23T14:00:00"
			}
		]
	}
}
```

### Status

| status | response content |
| --- | --- |
| 200 | 성공 |
| 400 | 잘못된 요청 |
| 500 | 서버오류 |

#### 400 - 잘못된 요청

```json
{
	"success": false,
	"status": 400,
	"code": "BAD_REQUEST",
	"message": "잘못된 요청입니다.",
	"timestamp": "2026-05-23T17:00:00",
	"result": null
}
```

#### 500 - 서버오류

```json
{
	"success": false,
	"status": 500,
	"code": "INTERNAL_SERVER_ERROR",
	"message": "서버 내부 오류가 발생했습니다.",
	"timestamp": "2026-05-23T17:00:00",
	"result": null
}
```

# 게시글 상세 조회

카테고리: 게시글
설명: 게시글의 내용을 조회합니다.
Method: GET
URL: /posts/{post_id}
사용자: 유저

### Request

| key | 설명 | value 타입 | 옵션 | Nullable | 예시 |
| --- | --- | --- | --- | --- | --- |
| post_id | 게시글 id | integer |  | notnull | 1 |

**Query parameter**

### Response

| key | 설명 | value 타입 | 옵션 | Nullable | 예시 |
| --- | --- | --- | --- | --- | --- |
| result.id | 게시글 id  | integer |  | not null | 1 |
| result.title | 게시글 제목 | string |  | not null | “첫 번째 게시글입니다.” |
| result.content | 게시글 본문 | string |  | not null | “본문 내용입니다.” |
| result.author | 작성자 | string |  | not null | "user1” |
| result.created_at | 작성 날짜 및 시간 | string |  | not null | “2026-05-23T14:00:00” |
| result.comments | 댓글 리스트 | array |  | - | {[ … ]} |
| result.comments[].id | 댓글 id | integer |  | not null | 101 |
| result.comments[].content | 댓글 내용 | string |  | not null | “댓글입니다.” |
| result.comments[].author | 댓글 작성자 | string |  | not null | “user2” |

**Example**

```jsx
{
    "success": true,
    "status": 200,
    "code": "SUCCESS",
    "message": "상세 조회에 성공했습니다.",
    "timestamp": "2026-05-23T17:00:00",
    "result": {
        "id": 45,
        "title": "첫 번째 게시글입니다.",
        "content": "이것은 본문 내용입니다.",
        "author": "user1",
        "created_at": "2026-05-23T15:00:00"
        "comments": [
	        {
		        "id": 101,
		        "content": "댓글입니다."
		        "author": "user2"
	        }
        ]
    }
}
```

### Status

| status | response content |
| --- | --- |
| 200 | 성공 |
| 400 | 잘못된 요청 |
| 500 | 서버오류 |

#### 400 - 잘못된 요청

```json
{
	"success": false,
	"status": 400,
	"code": "BAD_REQUEST",
	"message": "잘못된 요청입니다.",
	"timestamp": "2026-05-23T17:00:00",
	"result": null
}
```

#### 500 - 서버오류

```json
{
	"success": false,
	"status": 500,
	"code": "INTERNAL_SERVER_ERROR",
	"message": "서버 내부 오류가 발생했습니다.",
	"timestamp": "2026-05-23T17:00:00",
	"result": null
}
```

# 새 게시글 작성

카테고리: 게시글
설명: 새 게시글을 작성합니다.
Method: POST
URL: /posts
사용자: 유저

### Request

| key | 설명 | value 타입 | 옵션 | Nullable | 예시 |
| --- | --- | --- | --- | --- | --- |
| title | 게시글 제목 | string |  | not null | “첫 번째 게시글입니다.” |
| content | 게시글 본문 | string |  | not null | “본문 내용입니다.” |
| author | 작성자 | string |  | not null | “user1” |
|  |  |  |  |  |  |

**Example**

```jsx
{
	"title": “첫 번째 게시글입니다.”,
	"content": “본문 내용입니다.”,
	"author": “user1”
}
```

**Query parameter**

### Response

| key | 설명 | value 타입 | 옵션 | Nullable | 예시 |
| --- | --- | --- | --- | --- | --- |
| result.id | 생성된 게시글 id | integer |  | not null | 46 |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |

**Example**

```jsx
{
    "success": true,
    "status": 201,
    "code": "CREATED",
    "message": "게시글 작성에 성공했습니다.",
    "timestamp": "2026-05-23T17:15:00",
    "result": {
        "id": 46
    }
}
```

### Status

| status | response content |
| --- | --- |
| 201 | 성공 |
| 400 | 잘못된 요청 |
| 500 | 서버오류 |

#### 400 - 잘못된 요청

```json
{
	"success": false,
	"status": 400,
	"code": "BAD_REQUEST",
	"message": "잘못된 요청입니다.",
	"timestamp": "2026-05-23T17:00:00",
	"result": null
}
```

#### 500 - 서버오류

```json
{
	"success": false,
	"status": 500,
	"code": "INTERNAL_SERVER_ERROR",
	"message": "서버 내부 오류가 발생했습니다.",
	"timestamp": "2026-05-23T17:00:00",
	"result": null
}
```

# 게시글 삭제

카테고리: 게시글
설명: 게시글을 삭제합니다.
Method: DELETE
URL: /posts/{post_id}
사용자: 유저

### Request

| key | 설명 | value 타입 | 옵션 | Nullable | 예시 |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

**Example**

```jsx
{
	
}
```

**Query parameter**

| key | 설명 | value 타입 | 옵션 | Nullable | 예시 |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |
|  |  |  |  |  |  |

Path variable

| key | 설명 | value 타입 | 옵션 | Nullable | 예시 |
| --- | --- | --- | --- | --- | --- |
| post_id | 삭제할 게시글 id | integer |  | notnull | 46 |
|  |  |  |  |  |  |

### Response

| key | 설명 | value 타입 | 옵션 | Nullable | 예시 |
| --- | --- | --- | --- | --- | --- |
| result | 결과 데이터 | null |  | - | null |

**Example**

```jsx
{
    "success": true,
    "status": 200,
    "code": "SUCCESS",
    "message": "게시글 삭제에 성공했습니다.",
    "timestamp": "2026-05-23T17:20:00",
    "result": null
}
```

### Status

| status | response content |
| --- | --- |
| 200 | 성공 |
| 400 | 잘못된 요청 |
| 500 | 서버오류 |

#### 400 - 잘못된 요청

```json
{
	"success": false,
	"status": 400,
	"code": "BAD_REQUEST",
	"message": "잘못된 요청입니다.",
	"timestamp": "2026-05-23T17:00:00",
	"result": null
}
```

#### 500 - 서버오류

```json
{
	"success": false,
	"status": 500,
	"code": "INTERNAL_SERVER_ERROR",
	"message": "서버 내부 오류가 발생했습니다.",
	"timestamp": "2026-05-23T17:00:00",
	"result": null
}
```

# 댓글 작성

카테고리: 댓글
설명: 게시글에 댓글을 작성합니다.
Method: POST
URL: /posts/{post_id}/comments
사용자: 유저

# Request

| key | 설명 | value 타입 | 옵션 | Nullable | 예시 |
| --- | --- | --- | --- | --- | --- |
| content | 댓글 내용 | string |  | not null | “댓글입니다.” |
| author | 작성자 | string |  | not null | “user2” |

**Example**

```jsx
{
	"content": "댓글입니다.",
	"author": "user2"
}
```

**Query parameter**

| key | 설명 | value 타입 | 옵션 | Nullable | 예시 |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |
|  |  |  |  |  |  |

Path variable

| key | 설명 | value 타입 | 옵션 | Nullable | 예시 |
| --- | --- | --- | --- | --- | --- |
| post_id | 댓글 작성할 게시글 id | integer |  | not null | 45 |
|  |  |  |  |  |  |

# Response

| key | 설명 | value 타입 | 옵션 | Nullable | 예시 |
| --- | --- | --- | --- | --- | --- |
| result.comment_id | 생성된 댓글 id | integer |  | not null | 101 |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |

**Example**

```jsx
{
    "success": true,
    "status": 201,
    "code": "CREATED",
    "message": "댓글 작성에 성공했습니다.",
    "timestamp": "2026-05-23T18:15:00",
    "result": {
        "comment_id": 101
    }
}
```

# Status

| status | response content |
| --- | --- |
| 200 | 성공 |
| 400 | 잘못된 요청 |
| 500 | 서버오류 |

#### 400 - 잘못된 요청

```json
{
	"success": false,
	"status": 400,
	"code": "BAD_REQUEST",
	"message": "잘못된 요청입니다.",
	"timestamp": "2026-05-23T17:00:00",
	"result": null
}
```

#### 500 - 서버오류

```json
{
	"success": false,
	"status": 500,
	"code": "INTERNAL_SERVER_ERROR",
	"message": "서버 내부 오류가 발생했습니다.",
	"timestamp": "2026-05-23T17:00:00",
	"result": null
}
```

# 댓글 삭제

카테고리: 댓글
설명: 댓글을 삭제합니다.
Method: DELETE
URL: /comments/{comment_id}
사용자: 유저

# Request

| key | 설명 | value 타입 | 옵션 | Nullable | 예시 |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |
|  |  |  |  |  |  |

**Example**

```jsx
{
	
}
```

**Query parameter**

| key | 설명 | value 타입 | 옵션 | Nullable | 예시 |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |
|  |  |  |  |  |  |

Path variable

| key | 설명 | value 타입 | 옵션 | Nullable | 예시 |
| --- | --- | --- | --- | --- | --- |
| comment_id | 삭제할 댓글 id | integer |  | notnull | 101 |
|  |  |  |  |  |  |

# Response

| key | 설명 | value 타입 | 옵션 | Nullable | 예시 |
| --- | --- | --- | --- | --- | --- |
| result | 결과 데이터 | null |  | - | null |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |

**Example**

```jsx
{
    "success": true,
    "status": 200,
    "code": "SUCCESS",
    "message": "게시글 삭제에 성공했습니다.",
    "timestamp": "2026-05-23T17:20:00",
    "result": null
}
```

# Status

| status | response content |
| --- | --- |
| 200 | 성공 |
| 400 | 잘못된 요청 |
| 500 | 서버오류 |

#### 400 - 잘못된 요청

```json
{
	"success": false,
	"status": 400,
	"code": "BAD_REQUEST",
	"message": "잘못된 요청입니다.",
	"timestamp": "2026-05-23T17:00:00",
	"result": null
}
```

#### 500 - 서버오류

```json
{
	"success": false,
	"status": 500,
	"code": "INTERNAL_SERVER_ERROR",
	"message": "서버 내부 오류가 발생했습니다.",
	"timestamp": "2026-05-23T17:00:00",
	"result": null
}
```