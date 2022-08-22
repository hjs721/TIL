sqlite> SELECT * FROM users;
id  name  role_id
--  ----  -------
1   관리자   1
2   김철수   2
3   이영희   2
sqlite> SELECT * FROM role;
id  title
--  -----
1   admin
2   staff
3   staff
sqlite> SELECT * FROM articles;
id  title  content  user_id
--  -----  -------  -------
1   1번글    111      1
2   2번글    222      2
3   3번글    333      1
4   4번글    444

-- users와 각각의 역할을 출력
SELECT *
FROM users JOIN role
    ON users.role_id = role.id;
-- id  name  role_id  id  title
-- --  ----  -------  --  -----
-- 1   관리자   1        1   admin
-- 2   김철수   2        2   staff
-- 3   이영희   2        2   staff

-- staff(2) 사용자(users)를 역할과 함께 출력하시오
SELECT *
FROM users JOIN role
    ON users.role_id = role.id
WHERE role.id = 2;
-- id  name  role_id  id  title
-- --  ----  -------  --  -----
-- 2   김철수   2        2   staff
-- 3   이영희   2        2   staff

-- 사용자(users)와 각각의 역할을 이름의 내림차순으로 출력하시오
SELECT *
FROM users JOIN role
    ON users.role_id = role.id
ORDER BY name DESC;
-- id  name  role_id  id  title
-- --  ----  -------  --  -----
-- 3   이영희   2        2   staff
-- 2   김철수   2        2   staff
-- 1   관리자   1        1   admin

-- 모든 게시글을 사용자 정보와 함께 출력하시오
SELECT *
FROM articles LEFT JOIN users
    ON articles.user_id = users.id;
id  title  content  user_id  id  name  role_id        
-- --  -----  -------  -------  --  ----  -------        
-- 1   1번글    111      1        1   관리자   1
-- 2   2번글    222      2        2   김철수   2
-- 3   3번글    333      1        1   관리자   1
-- 4   4번글    444

-- 작성자가 있는 모든 게시글을 사용자 정보와 함께 출력하시오
SELECT *
FROM articles LEFT JOIN users
    ON articles.user_id = users.id
WHERE articles.user_id IS NOT NULL;
-- id  title  content  user_id  id  name  role_id
-- --  -----  -------  -------  --  ----  -------
-- 1   1번글    111      1        1   관리자   1
-- 2   2번글    222      2        2   김철수   2
-- 3   3번글    333      1        1   관리자   1

-- 모든 게시글과 모든 사용자 정보를 출력하시오
SELECT *
FROM articles FULL JOIN users
    ON articles.user_id = users.id;
-- id  title  content  user_id  id  name  role_id
-- --  -----  -------  -------  --  ----  -------
-- 1   1번글    111      1        1   관리자   1
-- 2   2번글    222      2        2   김철수   2
-- 3   3번글    333      1        1   관리자   1
-- 4   4번글    444
--                              3   이영희   2

-- users와 role의 CROSS JOIN의 결과를 출력하시오
SELECT *
FROM users CROSS JOIN role;