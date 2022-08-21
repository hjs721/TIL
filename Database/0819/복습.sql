-- gender가 1인 경우는 남자를, gender가 2인 경우는 여자를 출력
SELECT
	id,
	CASE
		WHEN gender = 1 THEN '남자'
		WHEN gender = 2 THEN '여자'
	END
FROM healthcare
LIMIT 5;

-- id  CASE
-- --  ----
-- 1   남자
-- 2   여자
-- 3   여자
-- 4   남자
-- 5   여자


-- gender가 1인 경우는 남자를, gender가 2인 경우는 여자를 출력
SELECT
	last_name || first_name AS 이름,
	CASE
		WHEN age <= 18 THEN '청소년'
		WHEN age <= 34 THEN '청년'
		WHEN age <= 46 THEN '장년'
		WHEN age <= 60 THEN '중년'
		ELSE '노년'
	END
FROM users
LIMIT 5;

-- 이름   CASE
-- ---  ----
-- 유정호  장년
-- 이경희  장년
-- 구정자  장년
-- 장미경  장년
-- 차영환  청년


-- users에서 가장 나이가 작은 사람의 수
-- 가장 나이가 작은 사람:
SELECT MIN(age) FROM users;
-- 서브 쿼리로 활용
SELECT COUNT(*) FROM users WHERE age = (SELECT MIN(age) FROM users);

-- COUNT(*)
-- --------
-- 39


-- users에서 평균 계좌 잔고보다 잔고가 높은 사람의 수
-- 평균 잔고:
SELECT AVG(balance) FROM users;
-- 서브 쿼리로 활용
SELECT COUNT(*) FROM users WHERE balance > (SELECT AVG(balance) FROM users);

-- COUNT(*)
-- --------
-- 222


-- users에서 유은정과 같은 지역에 사는 사람의 수
-- 유은정의 지역:
SELECT country FROM users WHERE last_name = '유' AND first_name = '은정';
-- 서브 쿼리로 활용
SELECT COUNT(*) FROM users WHERE country = (SELECT country FROM users WHERE last_name = '유' AND first_name = '은정');

-- COUNT(*)
-- --------
-- 101


-- 전체 인원과 평균 연봉, 평균 나이를 출력
SELECT COUNT(*), AVG(balance), AVG(age) FROM users;

SELECT
	(SELECT COUNT(*) FROM users) AS 총인원,
	(SELECT AVG(balance) FROM users) AS 평균연봉,
	(SELECT AVG(age) FROM users) AS 평균나이;

-- 총인원   평균연봉       평균나이
-- ----  ---------  ------
-- 1000  151456.89  27.346


-- users에서 이은정과 같은 지역에 사는 사람의 수
-- 이은정이 사는 지역
SELECT country FROM users WHERE last_name = '이' AND first_name = '은정';
-- country
-- -------
-- 전라북도
-- 경상북도
SELECT COUNT(*) FROM users WHERE country IN (SELECT country FROM users WHERE last_name = '이' AND first_name = '은정');
-- COUNT(*)
-- --------
-- 218


-- 특정 성씨에서 가장 어린 사람들의 이름과 나이
-- 특정 성씨에서 가장 어린 나이
SELECT last_name, MIN(age) FROM users GROUP BY last_name;
-- 서브 쿼리로 활용
SELECT first_name, last_name, age FROM users WHERE (last_name, age) IN (SELECT last_name, MIN(age) FROM users GROUP BY last_name) ORDER BY last_name;