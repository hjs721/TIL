# SQLite Aggregate Functions

- Aggregate function (집계 함수)
  - 값 집합에 대한 계산을 수행하고 단일 값을 반환
  - 여러 행으로부터 하나의 결과값을 반환하는 함수
- SELECT 구문에서만 사용됨
- 예시
  - 테이블 전체 행 수를 구하는 **COUNT(*)**
  - age 컬럼 전체 평균 값을 구하는 **AVG(age)**
- COUNT : 그룹의 항목 수를 가져옴
- AVG : 모든 값의 평균을 계산
- MAX : 그룹에 있는 모든 값의 최대값을 가져옴
- MIN : 그룹에 있는 모든 값의 최소값을 가져옴
- SUM : 모든 값의 합을 계산

### COUNT(레코드의 개수 조회하기)

```sqlite
SELECT COUNT(칼럼) FROM 테이블이름;
```

- users 테이블의 레코드 총 개수를 조회한다면?

```sqlite
SELECT COUNT(*) FROM users;
```

### AVG, SUM, MIN, MAX

- 위 함수들은 기본적으로 해당 컬럼이 숫자(INTEGER)일 때만 사용 가능

```sqlite
SELECT AVG(컬럼) FROM 테이블이름;
SELECT SUM(컬럼) FROM 테이블이름;
SELECT MIN(컬럼) FROM 테이블이름;
SELECT MAX(컬럼) FROM 테이블이름;
```

- 30살 이상인 사람들의 평균 나이는?

```sqlite
SELECT AVG(age) FROM users WHERE age >= 30;
```

- 계좌 잔액(balance)이 가장 높은 사람과 그 액수를 조회하려면?

```sqlite
SELECT MAX(balance), first_name FROM users;
```

- 나이가 30 이상인 사람의 계좌 평균 잔액을 조회하려면?

```sqlite
SELECT AVG(balance) FROM users WHERE age >= 30;
```