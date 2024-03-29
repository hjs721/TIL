# Database

### 개념

- 데이터베이스는 **체계화된 데이터**의 모임

- 여러 사람이 공유하고 사용할 목적으로 통합 관리되는 정보의 집합

- 논리적으로 연관된(하나 이상의) 자료의 모음으로 그 내용을 고도로 구조화함으로써 검색과 갱신의 효율화를 꾀한 것

- 즉, **몇 개의 자료 파일을 조직적으로 통합**하여 **자료 항목의 중복을 제거**하고 **자료를 구조화하여 기억**시켜놓은 **자료의 집합체**

  

### 장점

- 데이터 중복 최소화
- 데이터 무결성(정확한 정보를 보장)
- 데이터 일관성
- 데이터 독립성(물리적/논리적)
- 데이터 표준화
- 데이터 보안 유지





# RDB

### 관계형 데이터베이스(RDB, Relational Database)

- 서로 관련된 데이터를 저장하고 접근할 수 있는 데이터베이스 유형
- 키(key)와 값(value)들의 간단한 관계(relation)를 표(table) 형태로 정리한 데이터베이스

### 스키마(schema)

- 데이터베이스에서 자료의 구조, 표현방법, 관계 등 전반적인 **명세를 기술**한 것

### 테이블(table)

- 열(컬럼/필드)과 행(레코드/값)의 모델을 사용해 조직된 데이터 요소들의 집합
- 열 (column) : 각 열에 고유한 데이터 형식 지정
- 행 (row) : 실제 데이터가 저장되는 형태
- 기본키(Primary Key) : 각 행(레코드)의 고유 값
  - 반드시 설정해야 하며, 데이터베이스 관리 및 관계 설정 시 주요하게 활용됨





# RDBMS

- 관계형 데이터베이스 관리 시스템(RDBMS) :

  MySQL, SQLite, PostgreSQL, ORACLE, SQLServer, ...

### SQLite

- 서버 형태가 아닌 파일 형식으로 응용 프로그램에 넣어서 사용하는 **비교적 가벼운 데이터베이스**
- 구글 안드로이드 운영체제에 기본적으로 탑재된 데이터베이스이며, 임베디드 소프트웨어에도 많이 활용됨
- 오픈소스 프로젝트로, 자유롭게 사용가능하며 로컬에서 간단한 DB 구성을 할 수 있음

### SQLite Data Type

- NULL
- INTEGER
  - 크기에 따라 0, 1, 2, 3, 4, 6 또는 8바이트에 저장된 부호 있는 정수
- REAL
  - 8바이트 부동 소수점 숫자로 저장된 부동 소수점 값
- TEXT
- BLOB
  - 입력된 그대로 정확히 저장된 데이터(별다른 타입 없이 그대로 저장)

### SQLite Type Affinity (1/2)

- 특정 컬럼에 저장하도록 권장하는 데이터 타입

1. INTEGER
2. TEXT
3. BLOB
4. REAL
5. NUMERIC

- | Example Typenames From The CREATE TABLE Statement            | Resulting Affinity |
  | ------------------------------------------------------------ | ------------------ |
  | INT<br />INTEGER<br />TINYINT<br />SMALLINT<br />MEDIUMINT<br />BIGINT<br />UNSIGNED BIG INT<br />INT2<br />INT8 | INTEGER            |
  | CHRACTER(20)<br />VARCHAR(255)<br />VARYING CHARACTER(255)<br />NCHAR(55)<br />NATIVE CHARICTER(70)<br />NVARCHAR(100)<br />TEXT<br />CLOB | TEXT               |
  | BLOB ( no datatype specified)                                | BLOB               |
  | REAL<br />DOUBLE<br />DOUBLE PRECISION<br />FLOAT            | REAL               |
  | NUMERIC<br />DECIMAL(10,5)<br />BOOLEAN<br />DATE<br />DATETIME | NUMERIC            |

  

# SQL

### SQL(Structured Query Language)

- 관계형 데이터베이스 관리시스템의 **데이터 관리**를 위해 설계된 **특수 목적으로 프로그래밍된 언어**
- 데이터베이스 스키마 생성 및 수정
- 자료의 검색 및 관리
- 데이터베이스 객체 접근 조정 관리

- | 분류                                                     | 개념                                                         | 예시                                        |
  | -------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------- |
  | DDL - 데이터 정의 언어<br />(Data Definition Language)   | 관계형 데이터베이스 구조(테이블, 스키마)를 정의하기 위한 명령어 | CREATE<br />DROP<br />ALTER                 |
  | DML - 데이터 조작 언어<br />(Data Manipulation Language) | 데이터를 저장, 조회, 수정, 삭제 등을 하기 위한 명령어        | INSERT<br />SELECT<br />UPDATE<br />DELETE  |
  | DCL - 데이터 제어 언어<br />(Data Control Language)      | 데이터베이스 사용자의 권한 제어를 위해 사용하는 명령어       | GRANT<br />REVOKE<br />COMMIT<br />ROLLBACK |

### SQL Keywords - Data Manipulation Language

- INSERT : 새로운 데이터 삽입(추가)
- SELECT : 저장되어 있는 데이터 조회
- UPDATE : 저장되어 있는 데이터 갱신
- DELETE : 저장되어 있는 데이터 삭제



# Hello World!

### 테이블 생성 및 삭제

- 데이터베이스 생성하기
  - '.'은 sqlite에서 활용되는 명령어

```bash
$ sqlite3 tutorial.sqlite3
sqlite> .database
```

- csv 파일을 table로 만들기

```bash
sqlite> .mode csv
sqlite> .import hellodb.csv examples
sqlite> .tables
examples
```

- SELECT

```bash
SELECT * FROM examples;
```

- SELECT 확인하기
  - **SELECT 문은 특정 테이블 레코드(행) 정보를 반환!**

```bash
sqlite> SELECT * FROM examples;
1,"길동","홍",600,"충청도",010-0000-0000
```

- (Optinal) 터미널 View 변경하기

```bash
sqlite> SELECT * FROM examples;
1,"길동","홍",600,"충청도",010-0000-0000
sqlite> .headers.on
sqlite> SELECT * FROM examples;
id,first_name,last_name,age,country,phone
splite> .mode column
splite> SELECT * FROM examples;

```

- 진행 TIP - sqlite 확장프로그램 사용하기 (1/5)

  - sqlite 파일 우클릭 - Open Database

  ![sqlite1](Database.assets/sqlite1.png)

- 진행 TIP - sqlite 확장프로그램 사용하기 (2/5)

  - New Query 클릭

  ![sqlite2](Database.assets/sqlite2.png)

  - 우측 화면에 sql 명령어를 작성하는 페이지가 출력됨

  ![sqlite2_1](Database.assets/sqlite2_1.png)

- 진행 TIP - sqlite 확장프로그램 사용하기 (3/5)

  - 코드 작성 후 우클릭 - Run Query(전체 코드 실행) or Run Selected Query(선택 코드 실행)

  ![sqlite3](Database.assets/sqlite3.png)

- 진행 TIP - sqlite 확장프로그램 사용하기 (4/5)

  - 새로고침 아이콘 클릭 후 데이터베이스 변화 확인

  ![sqlite4](Database.assets/sqlite4.png)

- 진행 TIP - sqlite 확장프로그램 사용하기 (5/5)

  - 특정 코드만 실행 후 가장 우측 화면에서 결과 확인

  ![sqlite5](Database.assets/sqlite5.png)



- 테이블 생성 및 삭제 statement
  - CREATE TABLE : 데이터베이스에서 테이블 생성
  - DROP TABLE : 데이터베이스에서 테이블 제거

- CREATE
  - 테이블 생성
  - 테이블 생성 확인
  - 특정 테이블의 스키마 확인
- DROP
  - DROP
  - 삭제 확인
- 다음과 같은 스키마를 가지고 있는 calssmates 테이블을 만들고 확인

| column  | datatype |
| ------- | -------- |
| name    | TEXT     |
| age     | INT      |
| address | TEXT     |

- SQL

  - 테이블 생성 실습(2/2)

  ```sqlite
  CREATE TABLE classmates (
      name TEXT,
      age INT,
      address TEXT
  ); 
  ```

  - 터미널 창 확인

  ```bash
  sqlite> .schema classmates
  CREATE TABLE classmates (
      name TEXT,
      age INT,
      address TEXT
  );
  ```

- 필드 제약 조건
  - NOT NULL : NULL 값 입력 금지
  - UNIQUE : 중복 값 입력 금지(NULL 값은 중복 입력 가능)
  - PRIMARY KEY : 테이블에서 반드시 하나, NOT NULL + UNIQUE
  - FOREIGN KEY : 외래키. 다른 테이블의 Key
  - CHECK : 조건으로 설정된 값만 입력 허용
  - DEFAULT : 기본 설정 값
- 아래 테이블의 의미를 확인해보자

```sqlite
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER DEFAULT 1 CHECK (0 < age)
);
-- 숫자 id를 프라이머리 키로 가지는 students 테이블 생성
-- 컬럼 세 개 : 숫자 id, 문자열 name, 숫자 age
-- 이름은 비워둘 수 없음
-- 나이 디폴트값은 1이고, 0보다 크다는 조건을 체크(확인)하라 : 음수값은 런타임 에러 남
```





# CRUD

## CREATE

#### INSERT

- "Insert a single row into a table"
- 테이블에 단일 행 삽입

```sqlite
INSERT INTO 테이블_이름 (컬럼1, 컬럼2) VALUES (값1, 값2);
```

- 테이블에 정의된 모든 칼럼에 맞춰 순서대로 입력

```sqlite
INSERT INTO 테이블_이름 VALUES (값1, 값2, 값3)
```

- classmates 테이블에 이름이 홍길동이고, 나이가 23인 데이터를 넣어보자

```sqlite
INSERT INTO classmates (name, age) VALUES ('홍길동', 23);
```

```bash
sqlite> SELECT * FROM classmates;
name  age  address
----  ---  -------
홍길동   23
```

- classmates 테이블에 이름이 홍길동이고, 나이가 30이고, 주소가 서울인 데이터를 넣어보자

```sqlite
INSERT INTO classmates VALUES ('홍길동', 30, '서울');
```

```bash
sqlite> SELECT * FROM classmates;
name  age  address
----  ---  -------
홍길동   23
홍길동   30   서울
```

- 해당 bash 형태로 데이터가 기억되어도 괜찮을까?

- rowid : SQLite에서 PRIMARY KEY가 없는 경우 자동으로 증가하는 PK 칼럼

```bash
sqlite> SELECT rowid, * FROM classmates;
rowid  name  age  address
-----  ----  ---  -------
1      홍길동   23
2      홍길동   30   서울
```

- 비어 있는 주소

```bash
sqlite> SELECT * FROM classmates;
name  age  address
----  ---  -------
홍길동   23
홍길동   30   서울
```

- 지우고 새로 만들기

```sqlite
DROP TABLE classmates;
CREATE TABLE classmates (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INT NOT NULL,
    adrress TEXT NOT NULL
);
```



- Q. classmates 테이블에 이름이 홍길동이고, 나이가 30이고, 주소거 서울인 데이터를 넣어보자

  - 실패

  ```sqlite
  INSERT INTO classmates VALUES ('홍길동', 30, '서울');
  ```

  ```bash
  sqlite> INSERT INTO classmates VALUES ('홍길동', 30, '서울');
  Parse error: table classmates has 4 columns but 3 values were supplied
  ```

  **스키마에 id를 직접 작성했기 때문에 입력할 column들을 명시하지 않으면 자동으로 입력되지 않음**

  - 성공

  1. **id를 포함한 모든 values를 작성**

  ```sqlite
  INSERT INTO classmates VALUES (1, '홍길동', 30, '서울');
  ```

  2. **각 value에 맞는 column들을 명시적으로 작성**

  ```sqlite
  INSERT INTO classmates (name, age, address) VALUES ('홍길동', 30, '서울');
  ```

  결과:

  ```bash
  sqlite> INSERT INTO classmates VALUES (1, '홍길동', 30, '서울');
  sqlite> INSERT INTO classmates (name, age, address) VALUES ('홍길동', 30, '서울');
  sqlite> SELECT * FROM classmates;
  id  name  age  address
  --  ----  ---  -------
  1   홍길동   30   서울
  2   홍길동   30   서울
  ```



❗ 이번 실습에서는 rowid를 사용해서 편하게 진행하자! (테이블 삭제, 재생성)



- Q. INSERT 직접 해보기
  - 방금 새롭게 생성한 테이블에 다음과 같은 정보를 저장하고 확인해봅시다.
  - 각 정보는 이름 / 나이 / 주소로 구분됩니다.
    - 홍길동 / 30 / 서울
    - 김철수 / 30 / 제주
    - 이호영 / 26 / 인천
    - 박민희 / 29 / 대구
    - 최혜영 / 28 / 전주

```sqlite
INSERT INTO classmates VALUES 
('홍길동', 30, '서울'), 
('김철수', 30, '제주'), 
('이호영', 26, '인천'), 
('박민희', 29, '대구'), 
('최혜영', 28, '진주');
```

```bash
sqlite> SELECT * FROM classmates;
name  age  address
----  ---  -------
홍길동   30   서울
김철수   30   제주
이호영   26   인천
박민희   29   대구
최혜영   28   진주
```



## READ

### SELECT

- "Query data from a table"
- 테이블에서 데이터를 조회
- SELECT 문은 SQLite에서 가장 기본이 되는 문이며 다양한 절(clause)와 함께 사용
  - ORDER BY, DISTINCT, WHERE, LIMIT, GROUP BY ...

- [SQLite SELECT - Querying Data From a Single Table (sqlitetutorial.net)](https://www.sqlitetutorial.net/sqlite-select/)

### LIMIT

- "Constrain the number of rows returned by a query"
- 쿼리에서 반환되는 행 수를 제한
- 특정 행부터 시작해서 조회하기 위해 **OFFSET** 키워드와 함께 사용하기도 함

### WHERE

- "Specify the serach condition for rows returned by the query"
- 쿼리에서 반환된 행에 대한 특정 검색 조건을 지정

### SELECT DISTINCT

- "Remove duplicate rows in the result set"
- 조회 결과에서 중복 행을 제거
- DISTINCT 절은 SELECT 키워드 바로 뒤에 작성해야 함



### 실습

- classmates 테이블에서 id, name 칼럼 값만 조회하라

```sqlite
SELECT rowid, name FROM classmates;
```

```bash
sqlite> SELECT rowid, name FROM classmates;
rowid  name
-----  ----
1      홍길동
2      김철수
3      이호영
4      박민희
5      최혜영
```

- classmates 테이블에서 id, name 칼럼 값을 하나만 조회하라

```sqlite
SELECT rowid, name FROM classmates LIMIT 1;
```

```bash
sqlite> SELECT rowid, name FROM classmates LIMIT 1; 
rowid  name
-----  ----
1      홍길동
```

- classmates 테이블에서 id, name 칼럼 값을 세 번째에 있는 하나만 조회하라

```sqlite
SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;
```

```bash
sqlite> SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;FFSET 2;
rowid  name
-----  ----
3      이호영
```



### OFFSET 

- 처음부터 주어진 요소나 지점까지의 차이를 나타내는 정수형

- ex. 문자열 'abcdef'에서 문자 'c'는 시작점 'a'에서 2까지의 OFFSET을 지님

  SELECT * FROM MY_TABLE LIMIT 10 **OFFSET 5**

  - 6번째 행부터 10개 행을 조회(6번째 행부터 10개를 출력)
  - 0부터 시작함



### 실습

- classmates 테이블에서 id, name 컬럼 값 중에 주소가 서울인 경우의 데이터를 조회하라

```sqlite
SELECT * FROM classmates WHERE address = '서울';
```

```bash
sqlite> SELECT * FROM classmates WHERE address = '서
울';
name  age  address
----  ---  -------
홍길동   30   서울
```

- classmates 테이블에서 age 값 전체를 중복없이 조회하라

```sqlite
SELECT DISTINCT age FROM classmates;
```

```bash
sqlite> SELECT DISTINCT age FROM classmates;        
age
---
30
26
29
28
```

