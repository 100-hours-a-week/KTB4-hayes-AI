### LangChain

- llm 개발을 위한 프레임워크

### Messages

- Chat Model과 주고받는 역할과 내용을 포함해서 구조화된 객체들의 집합

### LCEL

- 파이프 연산자로 Runnable 컴포넌트를 선언적으로 연결하여 체인을 구성하는 랭체인 문법체계

### PromptTemplate

- 프롬프트 문자열을 객체로 관리하고 값을 주입하여 프롬프트를 완성된 형태로 생성하는 클래스

### ChatPromptTemplate

- 역할별 메시지 리스트를 구성하는 프롬프트 템플릿 클래스

### FewShotPromptTemplate

- 입출력 예시를 프롬프트에 삽입하여 llm이 원하는 형식과 패턴으로 응답하도록 유도하는 프롬프트 템플릿 클래스

### MessagesPlaceholder

- ChatPromptTemplate 안에서 실행 시점에 메시지 리스트가 삽입될 위치를 지정하는 컴포넌트

### Structured Output

- llm의 응답을 사전에 정의한 스키마에 맞춰 객체로 반환하는 방식

### JsonOutputParser

- llm의 응답을 json 형태로 파싱하는 출력 파서 클래스

### PydanticOutputParser

- llm의 응답을 Pydantic로 파싱하여 타입 검증과 필드 접근을 제공하는 출력 파서 클래스

### Runnable Interface

- 프롬프트, 모델, 파서, 커스텀 함수처럼 서로 다른 객체를 같은 방식으로 실행하기 위한 표준 메서트 규칙

### RunnablePassthrough

- LCEL 체인에서 입력 데이터를 변형 없이 다음 단계로 전달하거나 새 키를 추가하는 Runnable 유틸리티 클래스

### RunableParallel

- 여러 Runnable을 동일한 입력으로 동시에 실행하고, 각 결과를 지정한 키에 매핑하여 하나의 딕셔너리로 합쳐 반환하는 Runnable 유틸리티 클래스

### RunnableBranch

- 입력 조건에 따라 서로 다른 Runnable을 실행하도록 분기하는 유틸리티 클래스

### RunnableWithMessageHistory

- 기존 LECL 체인을 감싸서 세션 ID를 기준으로 대확 이력을 자동으로 불러오고 저장하는 Runnable 래퍼 클래스

### Message Trimming

- 대화 이력이 llm의 컨텍스트 한도를 초과하지 않도록 정해진 기준으로 메시지를 제거하는 처리

### Document

- 랭체인에서 문서 한 조각을 표현하는 데이터 객체

### Document Loader

- 다양한 형식의 외부 데이터를 읽어 랭체인의 Document 객체 리스트로 반환하는 컴포넌트의 표준 인터페이스

### TextLoader

- 단일 텍스트 파일을 읽어 한 개의 Document 객체로 변환하는 구현체

### PyPDFLoader

- Python의 pypdf라이브러리를 내부적으로 사용하여 pdf파일을 읽고 페이지마다 한개의 Document 객체로 변환하는 구현체

### WebBaseLoader

- URL을 받아 HTML을 가져온 뒤 BeautifulSoup로 파싱하여 본문 텍스트를 Document 객체로 변환하는 구현체

### DirectoryLoader

- 지정된 디렉토리 안의 여러 파일을 glob 패턴으로 골라 내부 로더로 일괄 처리하여 Document 객체로 변환하는 구현체
