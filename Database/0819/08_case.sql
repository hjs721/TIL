-- 단순 조회
SELECT id, gender
FROM healthcare
LIMIT 5;

-- id  gender
-- --  ------
-- 1   1
-- 2   2
-- 3   2
-- 4   1
-- 5   2


-- 성별 1(남자), 2(여자)
SELECT
    id,
    CASE
        WHEN gender = 1 THEN '남자'
        WHEN gender = 2 THEN '여자'
        -- ELSE
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


-- 흡연(smoking)
SELECT DISTINCT smoking FROM healthcare;
-- smoking
-- -------
-- 1
-- 3
-- 2
--
-- 값에 공백도 존재함(NULL이 아님)
SELECT
    id,
    smoking,
    CASE
        WHEN smoking = 1 THEN '비흡연자'
        WHEN smoking = 2 THEN '흡연자'
        WHEN smoking = 3 THEN '헤비스모커'
        ELSE '무응답'
    END
FROM healthcare
LIMIT 10;


-- 나이에 따라서 구분
-- 청소년(~18), 청년(~34), 중장년(~65)
SELECT
    first_name,
    last_name,
    age,
    CASE
        WHEN age <= 18 THEN '청소년'
        WHEN age <= 34 THEN '청년'
        WHEN age <= 65 THEN '중년'
        ELSE '노년'
    END
FROM users
LIMIT 10;
-- first_name  last_name  age  CASE
-- ----------  ---------  ---  ----
-- 정호          유          40   중년
-- 경희          이          36   중년
-- 정자          구          37   중년
-- 미경          장          40   중년
-- 영환          차          30   청년
-- 서준          이          26   청년
-- 주원          민          18   청소년
-- 예진          김          33   청년
-- 서현          김          23   청년
-- 서윤          오          22   청년