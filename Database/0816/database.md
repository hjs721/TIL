## 데이터베이스
- 데이터베이스는 체계화된 데이터의 모임

- 여러 사람이 공유하고 사용할 목적으로 통합 관리되는 정보의 집합

- 몇 개의 자료 파일을 조직적으로 통합하여...

- 데이터베이스로 얻는 장점들

  - 데이터 중복 최소화

  - 데이터 무결성(정확한 정보를 보장)

  - 데이터 일관성

  - 데이터 독립성(물리적/논리적)

  - 데이터 표준화

  - 데이터 보안 유지

### RDB
- 스키마(schema)

  - 데이터베이스에서 자료의 구조, 표현방법, 관계 등 전반적인 명세를 기술한 것

  - 타입 지정 가능. INT, TEXT, ...

- 테이블

  - 열(컬럼/필드)과 행(레코드/값)의 모델을 사용해 조직된 데이터 요소들의 집합

- 열(column) : 각 열에 고유한 데이터 형식 지정

- 행(row) : 실제 데이터가 저장되는 형태

- 기본 키(Primary Key) : 각 행(레코드)의 고유 값

  - 반드시 설정해야 하며, 데이터베이스 관리 및 관계 설정 시에 주요하게 활용됨

### RDBMS
- 관계형 데이터베이스 관리 시스템(RDBMS)

  - 관계형 모델을 기반으로 하는 데이터베이스 관리시스템을 의미

  - SQLite, MySQL, ORACLE 등...

- SQLite

  - 서버 형태가 아닌 파일 형식으로 응용 프로그램에 넣어서 사용하는 **비교적 가벼운 데이터베이스**

  - 구글 안드로이드 운영체제에 기본적으로 탑재된 데이터베이스이며, 임베디드 소프트웨어에도 많이 활용됨

  - 로컬에서 간단한 DB 구성을 할 수 있으며, 오픈소스 프로젝트이기 때문에 자유롭게 이용 가능

- SQLite 데이터 타입 : INTEGER, TEXT, BLOB, REAL, NUMERIC

### SQL
- SQL (Structed Query Language)

  - 관계형 데이터베이스 관리 시스템의 **데이터 관리를 위해 특수 목적으로 만들어진 프로그래밍 언어**

  - 데이터베이스 스키마 생성 및 수정

  - 자료의 검색 및 관리

  - 데이터베이스 객체 어쩌구

- DDL(Data Definition Language) - 데이터 정의 언어
관계형 데이터베이스 구조(테이블, 스키마)를 정의하기 위한 명령어

### Hello World!
## 테이블 생성 및 삭제
- 데이터베이스 생성하기

### CRUD

```sqlite
CREATE TABLE classmates (
    name TEXT NOT NULL,
    age INT NOT NULL,
    adress TEXT NOT NULL
);
```

# 값 추가
INSERT INTO classmates VALUES
('홍길동', 30, '서울'),
('김철수', 30, '제주'),
('류호피', 30, '남경'),
('강희제', 30, '남경');

# 특정 컬럼을 뽑아서 조회
SELECT rowid, name FROM classmates;

# 하나만 조회
SELECT rowid, name FROM classmates LIMIT 1;

# N번째 행을 하나만 조회(OFFSET숫자는 인덱스)
SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;

SELECT * FROM classmates WHERE adress='서울';

SELECT name FROM classmates WHERE age >= 30;

SELECT DISTINCT age FROM classmates;

SELECT DISTINCT adress FROM classmates;

- 삭제
DELETE FROM calssmates WHERE rowid=1;

INSERT INTO calssmates VALUES ('이환매', 35, '대전');