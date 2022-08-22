-- INNER JOIN
-- A와 B 테이블에서 값이 일치하는 것들만
SELECT *
FROM users JOIN role
    ON users.role_id = role.id;

SELECT
    users.name,
    role.title
FROM users JOIN role
    ON users.role_id = role.id;

-- 스태프(2)만 출력
SELECT *
FROM users JOIN role
    On users.role_id = role.id
WHERE role.id = 2;

-- 이름을 내림차순으로 출력하세요
SELECT *
FROM users JOIN role
    On users.role_id = role.id
ORDER BY users.name DESC;


-- LEFT OUTER JOIN
SELECT *
FROM articles LEFT OUTER JOIN users
    ON articles.user_id = users.id;

SELECT *
FROM articles LEFT OUTER JOIN users
    ON articles.user_id = users.id
WHERE articles.user_id IS NOT NULL;

-- FULL OUTER JOIN
SELECT *
FROM articles FULL OUTER JOIN users
    ON articles.user_id = users.id;


-- CROSS JOIN
SELECT *
FROM users CROSS JOIN role;


-- 3개의 테이블 조인
SELECT * 
FROM articles
    JOIN users
        ON articles.user_id = users.id
    JOIN role
        ON users.role_id = role.id;