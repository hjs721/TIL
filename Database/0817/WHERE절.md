# WHERE

### 기본 세팅

- Table users 생성

```sqlite
CREATE TABLE users (
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	age INTEGER NOT NULL,
	country TEXT NOT NULL,
	phone TEXT NOT NULL,
	balance INTEGER NOT NULL
);
```

- csv 파일 정보를 테이블에 적용하기 (참조: 05_users.sql)

```sqlite
sqlite> .mode csv
sqlite> .import users.csv users
sqlite> .tables
classmates exapmles users
```



### WHERE 절에서 사용할 수 있는 연산자

- 비교 연산자

  - =, >, >=, <, <= 는 숫자 혹은 문자 값의 대소, 동일 여부를 확인하는 연산자

- 논리 연산자

  - AND : 앞에 있는 조건과 뒤에 있는 조건이 모두 참인 경우
  - OR : 앞의 조건이나 뒤의 조건이 참인 경우
  - NOT : 뒤에 오는 조건의 결과를 반대로

- 주의!

  ```sqlite
  -- 1. 키가 175이거나, 키가 183이면서 몸무게가 80인 사람
  WHERE HEIGHT = 175 OR HEIGHT = 183 AND WEIGHT = 80
  -- 2. 키가 175 또는 183인 사람 중에서 몸무게가 80인 사람
  WHERE (HEIGHT = 175 OR HEIGHT = 183) AND WEIGHT = 80
  ```



### SQL 사용할 수 있는 연산자

- BETWEEN 값1 AND 값2
  - 값1과 값2 사이의 비교 (값1 <= 비교값 <= 값2)
- IN (값1, 값2, ...)
  - 목록 중에서 값이 하나라도 일치하면 성공
- LIKE
  - 비교 문자열과 형태 일치
  - 와일드카드(% : 0개 이상 문자, _ : 1개 단일 문자)
- IS NULL / IS NOT NULL
  - NULL 여부를 확인할 때는 항상 = 대신에 IS를 활용
- 부정 연산자
  - 같지 않다 (!=, ^=, <>)
  - ~와 같지 않다 (NOT  칼럼명 =)
  - ~보다 크지 않다 (NOT 칼럼명 >)

- 연산자 우선순위
  - 1순위 : 괄호 ()
  - 2순위 : NOT
  - 3순위 : 비교 연산자, SQL
  - 4순위 : AND
  - 5순위 : OR