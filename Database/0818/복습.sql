SELECT * FROM users LIMIT 1;


-- 문자열 합치기
-- 성+이름으로 5명을 출력해보자
SELECT 
    last_name || first_name 이름,
    age,
    country,
    phone,
    balance
FROM users
LIMIT 5;

-- 이름   age  country  phone          balance
-- ---  ---  -------  -------------  -------
-- 유정호  40   전라북도     016-7280-2855  370
-- 이경희  36   경상남도     011-9854-5133  5900
-- 구정자  37   전라남도     011-4177-8170  3100
-- 장미경  40   충청남도     011-9079-4419  250000
-- 차영환  30   충청북도     011-2921-4284  220


-- 문자열 길이 LENGTH
SELECT
    LENGTH(first_name),
    first_name
FROM users
LIMIT 5;

-- LENGTH(first_name)  first_name
-- ------------------  ----------
-- 2                   정호
-- 2                   경희
-- 2                   정자
-- 2                   미경
-- 2                   영환


-- 문자열 변경 REPLACE
SELECT
    first_name, REPLACE(phone, '-', '')
FROM users
LIMIT 5;

-- first_name  REPLACE(phone, '-', '')
-- ----------  -----------------------
-- 정호          01672802855
-- 경희          01198545133
-- 정자          01141778170
-- 미경          01190794419
-- 영환          01129214284


-- 숫자 활용
-- 나눗셈 나머지
SELECT MOD(5, 2)
FROM users
LIMIT 1;
-- MOD(5, 2)
-- ---------
-- 1.0

-- 올림, 내림, 반올림
SELECT CEIL(3.14), FLOOR(3.14), ROUND(3.14)
FROM users
LIMIT 1;
-- CEIL(3.14)  FLOOR(3.14)  ROUND(3.14)
-- ----------  -----------  -----------
-- 4.0         3.0          3.0

-- 제곱근
SELECT SQRT(9)
FROM users
LIMIT 1;
-- SQRT(9)
-- -------
-- 3.0

-- 9^2
SELECT POWER(9, 2)
FROM users
LIMIT 1;
-- POWER(9, 2)
-- -----------
-- 81.0


-- users에서 각 성(last_name)씨가 몇 명씩 있는지 조회한다면?
SELECT last_name, COUNT(*)
FROM users
GROUP BY last_name;
-- last_name  COUNT(*)
-- ---------  --------
-- 강          23
-- 고          10
-- 곽          4
-- 구          2
-- ...

-- GROUP BY에서 활용하는 칼럼을 제외하고는 집계함수를 쓰자!!
SELECT last_name, age, COUNT(*)
FROM users
GROUP BY last_name;
-- last_name  age  COUNT(*)
-- ---------  ---  --------
-- 강          20   23
-- 고          34   10
-- 곽          25   4
-- 구          37   2
-- ...
-- 여기서 age는 전혀 의미가 없음


-- GROUP BY는 결과가 정렬되지 않음. 기존순서와 바뀜!
-- 원칙적으로 내가 정렬해서 보고 싶으면 ORDER BY 사용해야!!!
SELECT *
FROM users
LIMIT 5;
-- first_name  last_name  age  country  phone          balance
-- ----------  ---------  ---  -------  -------------  -------
-- 정호          유          40   전라북도     016-7280-2855  370
-- 경희          이          36   경상남도     011-9854-5133  5900
-- 정자          구          37   전라남도     011-4177-8170  3100
-- 미경          장          40   충청남도     011-9079-4419  250000
-- 영환          차          30   충청북도     011-2921-4284  220

SELECT last_name, COUNT(*)
FROM users
GROUP BY last_name
LIMIT 5;
-- last_name  COUNT(*)
-- ---------  --------
-- 강          23
-- 고          10
-- 곽          4
-- 구          2
-- 권          17


-- GROUP BY에서 WHERE를 쓰고 싶을 때
-- 100번 이상 등장한 성만 출력하고 싶음:
SELECT last_name, COUNT(last_name)
FROM users
WHERE COUNT(last_name) > 100
GROUP BY last_name;
-- 오류 발생! WHERE 실행순서가 앞서기 때문에 그룹화가 작동하지 않음
-- Parse error: misuse of aggregate: COUNT()
--   LECT last_name, COUNT(last_name) FROM users WHERE COUNT(last_name) > 100 GROUP

-- 조건에 따른 GROUP을 하려면 HAVING을 써야함!!!!!
SELECT last_name, COUNT(last_name)
FROM users
GROUP BY last_name
HAVING COUNT(last_name) > 100;
-- last_name  COUNT(last_name)
-- ---------  ----------------
-- 김          268
-- 이          179

SELECT last_name, COUNT(last_name)
FROM users
GROUP BY last_name
HAVING COUNT(last_name) > 50
ORDER BY last_name
LIMIT 3;
-- last_name  COUNT(last_name)
-- ---------  ----------------
-- 김          268
-- 박          98
-- 이          179

-- ALTER TABLE
-- title과 content라는 컬럼을 가진 articles 라는 이름의 table을 새롭게 만들어보세요! (두 컬럼 모두 비어있으면 안 되며, rowid를 사용합니다.)
CREATE TABLE articles (
	title TEXT NOT NULL,
	content TEXT NOT NULL
);

-- articles 테이블에 값을 추가해보세요! (title은 '1번제목', content는 '1번내용')
INSERT INTO articles VALUES ('1번제목', '1번내용');

-- 방금 만든 테이블의 이름을 변경해보기
ALTER TABLE articles RENAME TO news;

-- 새로 만든 컬럼 이름은 created_at이며, TEXT 타입에 NULL 설정!
ALTER TABLE news ADD COLUMN created_at TEXT NOT NULL;
-- 이러면 오류남

-- NOT NULL 설정 없이 추가하기
ALTER TABLE news ADD COLUMN created_at TEXT;
INSERT INTO news VALUES ('제목', '내용', datetime('now'));

-- 기본값(DEFAULT) 설정하기
ALTER TABLE news ADD COLUMN subtitle TEXT NOT NULL DEFAULT '소제목';