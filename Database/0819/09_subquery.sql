-- 가장 나이가 작은 사람의 수
-- 1
SELECT age, COUNT(*)
FROM users
GROUP BY age
ORDER BY age
LIMIT 1;
-- age  COUNT(*)
-- ---  --------
-- 15   39



-- 확인해보기
SELECT MIN(age)
FROM users;
SELECT COUNT(*)
FROM users
WHERE age = 15;

-- 서브 쿼리
SELECT COUNT(*)
FROM users
WHERE age = (SELECT MIN(age) FROM users);

-- COUNT(*)
-- --------
-- 39



-- 평균 계좌 잔고보다 잔고가 높은 사람의 수
-- 평균 계좌
SELECT AVG(balance) FROM users;

-- 서브 쿼리로 활용
SELECT COUNT(*)
FROM users
WHERE balance > (SELECT AVG(balance) FROM users);

-- COUNT(*)
-- --------
-- 222


-- 유은정과 같은 지역에 사는 사람의 수
SELECT country
FROM users
WHERE last_name = '유' AND first_name = '은정';

SELECT COUNT(*)
FROM users
WHERE country = (SELECT country FROM users WHERE last_name = '유' AND first_name = '은정');

-- COUNT(*)
-- --------
-- 101



-- 전체 인원과 평균 연봉, 평균 나이
SELECT COUNT(*), AVG(balance), AVG(age) FROM users;

SELECT
    (SELECT COUNT(*) FROM users) AS 총인원,
    (SELECT AVG(balance) FROM users) AS 평균연봉,
    (SELECT AVG(age) FROM users) AS 평균나이;


-- 이은정
SELECT
    country
FROM users
WHERE last_name = '이' AND first_name = '은정';
-- country
-- -------
-- 전라북도
-- 경상북도

SELECT
    COUNT(*)
FROM users
WHERE country = (SELECT country FROM users WHERE last_name = '이' AND first_name = '은정');
-- COUNT(*)
-- --------
-- 115

SELECT country, COUNT(*)
FROM users
GROUP BY country;

SELECT
    COUNT(*)
FROM users
WHERE country IN (SELECT country FROM users WHERE last_name = '이' AND first_name = '은정');
-- COUNT(*)
-- --------
-- 218
-- =대신 IN을 사용하면 전라북도와 경상북도 수가 합쳐서 나옴



-- 특정 성씨에서 가장 어린 사람들의 이름과 나이
-- 특정 성씨별로 그룹화해서 가장 어린 나이 찾기
SELECT
    last_name,
    MIN(age)
FROM users
GROUP BY last_name;

SELECT
    last_name,
    first_name,
    age
FROM users
WHERE (last_name, age) IN (
    SELECT
        last_name,
        MIN(age)
    FROM users
    GROUP BY last_name)
ORDER BY last_name;