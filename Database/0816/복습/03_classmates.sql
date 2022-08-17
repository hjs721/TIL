-- 실습에서는 rowid로 편하게 진행
DROP TABLE classmates;
CREATE TABLE classmates (
    name TEXT NOT NULL,
    age INT NOT NULL,
    address TEXT NOT NULL
);

INSERT INTO classmates VALUES 
('홍길동', 30, '서울'), 
('김철수', 30, '제주'), 
('이호영', 26, '인천'), 
('박민희', 29, '대구'), 
('최혜영', 28, '진주');

-- id, name 칼럼 값만 조회
SELECT rowid, name FROM classmates;
-- rowid  name
-- -----  ----
-- 1      홍길동
-- 2      김철수
-- 3      이호영
-- 4      박민희
-- 5      최혜영

--  id, name 칼럼 값을 하나만 조회
SELECT rowid, name FROM classmates LIMIT 1;
-- rowid  name
-- -----  ----
-- 1      홍길동

-- id, name 칼럼 값을 세 번째에 있는 하나만 조회
SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;
-- rowid  name
-- -----  ----
-- 3      이호영

SELECT * FROM classmates WHERE address = '서울';
-- name  age  address
-- ----  ---  -------
-- 홍길동   30   서울

SELECT DISTINCT age FROM classmates;
-- age
-- ---
-- 30
-- 26
-- 29
-- 28