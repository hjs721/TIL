-- 테이블 생성 실습(2/2)
CREATE TABLE classmates (
    name TEXT,
    age INT,
    address TEXT
); 

-- 이름 홍길동, 나이 23인 데이터를 넣어보자
INSERT INTO classmates (name, age) VALUES ('홍길동', 23);
-- 이름 홍길동, 나이 30, 주소 서울인 데이터를 넣어보자
INSERT INTO classmates VALUES ('홍길동', 30, '서울');

SELECT rowid, * FROM classmates;
-- rowid는 SQLite에서 자동으로 제공하고 있는 PK. 값이 1씩 증가하는 모습을 보임
-- rowid  name  age  address
-- -----  ----  ---  -------
-- 1      홍길동   23
-- 2      홍길동   30   서울


-- 주소가 비어있음. 테이블 지우고 새로 만들기
DROP TABLE classmates;
CREATE TABLE classmates (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INT NOT NULL,
    address TEXT NOT NULL
);

-- INSERT INTO classmates VALUES ('홍길동', 30, '서울');
-- Parse error: table classmates has 4 columns but 3 values were supplied
INSERT INTO classmates VALUES (1, '홍길동', 30, '서울');
INSERT INTO classmates (name, age, address) VALUES ('홍길동', 30, '서울');


CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER DEFAULT 1 CHECK (0 < age)
);

-- 음수 나이를 넣어본다면?
INSERT INTO students VALUES (1, '홍길동', -3);
-- Runtime error: CHECK constraint failed: 0 < age (19)

