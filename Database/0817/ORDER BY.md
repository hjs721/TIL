# ORDER BY

## ORDER BY

- "sort a result set of a query"
- 조회 결과 집합을 정렬
- SELECT 문에 추가하여 사용
- 정렬 순서를 위한 2개의 keyword 제공
  - ASC - 오름차순(default)
  - DESC - 내림차순

- 특정 컬럼을 기준으로 데이터를 정렬해서 조회하기

```sqlite
SELECT * FROM 테이블이름 ORDER BY 컬럼 ASC;
SELECT * FROM 테이블이름 ORDER BY 컬럼 DESC;
```

### 실습

- users에서 나이 순으로 오름차순 정렬하여 상위 10개만 조회한다면?

```sqlite
SELECT * FROM users ORDER BY age ASC LIMIT 10;
```

- 나이 순, 성 순으로 오름차순 정렬하여 상위 10개만 조회한다면?

```sqlite
SELECT * FROM users ORDER BY age, last_name LIMIT 10;
```

- 계좌 잔액 순으로 내림차순 정렬하여 해당 유저의 성과 이름을 10개만 조회한다면?

```sqlite
SELECT last_name, first_name FROM users ORDER BY balance DESC LIMIT 10;
```

