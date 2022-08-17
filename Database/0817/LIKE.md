# LIKE

- "query data based on pattern matching"
- 패턴 일치를 기반으로 데이터를 조회하는 방법
- SQLite는 패턴 구성을 위한 2개의 wildcards를 제공
  - % (percent sign) : 0개 이상의 문자
  - _ (underscore) : 임의의 단일 문자



### Wildcards 2가지 패턴

|                      %                       |                       _                       |
| :------------------------------------------: | :-------------------------------------------: |
| 이 자리에 문자열이 있을 수도, 없을 수도 있다 | 반드시 이 자리에 한 개의 문자가 존재해야 한다 |

- LIKE statement : 패턴을 확인하여 해당하는 값을 조회하기

```sqlite
SELECT % FROM 테이블이름 WHERE 컬럼 LIKE '패턴';
```

- wildcards 사용 예시

| 와일드카드 패턴    | 의미                                          |
| ------------------ | --------------------------------------------- |
| 2%                 | 2로 시작하는 값                               |
| %2                 | 2로 끝나는 값                                 |
| %2%                | 2가 들어가는 값                               |
| _2%                | 아무 값이 하나 있고 두 번째가 2로 시작하는 값 |
| 1_ _ _             | 1로 시작하고 총 4자리인 값                    |
| 2_ % _ % / 2 _ _ % | 2로 시작하고 적어도 3자리인 값                |



### 실습

- users 테이블에서 나이가 20대인 사람만 조회한다면?

```sqlite
SELECT * FROM users WHERE age LIKE '2_';
```

- users 테이블에서 지역 번호가 02인 사람만 조회한다면?

```sqlite
SELECT * FROM users WHERE phone LIKE '02%';
```

- users 테이블에서 이름이 '준'으로 끝나는 사람만 조회한다면?

```sqlite
SELECT * FROM users WHERE first_name LIKE '%준';
```

- users 테이블에서 중간 번호가 5114인 사람만 조회한다면?

```sqlite
SELECT * FROM users WHERE phone LIKE '%-5114-%';
```

