-- users 테이블에서 age가 30 이상인 유저의 모든 컬럼 정보를 조회하려면?
SELECT * FROM users WHERE age >= 30;
-- first_name  last_name  age  country  phone          balance
-- ----------  ---------  ---  -------  -------------  -------
-- 정호          유          40   전라북도     016-7280-2855  370
-- 경희          이          36   경상남도     011-9854-5133  5900
-- 정자          구          37   전라남도     011-4177-8170  3100
-- 미경          장          40   충청남도     011-9079-4419  250000
-- 영환          차          30   충청북도     011-2921-4284  220
-- 예진          김          33   충청북도     010-5123-9107  3700
-- ...

-- users 테이블에서 age가 30 이상인 유저 이름만 조회하려면?
SELECT first_name FROM users WHERE age >= 30;
-- sqlite> SELECT first_name FROM users WHERE age >= 30;
-- first_name
-- ----------
-- 정호
-- 경희
-- 정자
-- 미경
-- 영환
-- 예진
-- 하은
-- 영일
-- ...


-- users 테이블에서 age가 30 이상, 성이 '김'인 유저의 나이와 이름을 조회하려면?
SELECT age, first_name FROM users WHERE age >= 30 AND last_name = '김';
-- sqlite> SELECT age, first_name FROM users WHERE age >= 30 AND last_name = '김';
-- age  first_name
-- ---  ----------
-- 33   예진
-- 35   영일
-- 38   은주
-- 37   미영
-- 30   은영
-- ...


-- users 테이블의 레코드 총 개수를 조회한다면?
SELECT COUNT(*) FROM users;
-- COUNT(*)
-- --------
-- 1000


-- 30살 이상인 사람들의 평균 나이는?
SELECT AVG(age) FROM users WHERE age >= 30;
-- AVG(age)
-- ----------------
-- 35.1763285024155


-- 계좌 잔액(balance)이 가장 높은 사람과 그 액수를 조회하려면?
SELECT MAX(balance), first_name FROM users;
-- MAX(balance)  first_name
-- ------------  ----------
-- 1000000       순옥


-- 나이가 30 이상인 사람의 계좌 평균 잔액을 조회하려면?
SELECT AVG(balance) FROM users WHERE age >= 30;
-- AVG(balance)
-- ----------------
-- 153541.425120773


-- users 테이블에서 나이가 20대인 사람만 조회한다면?
SELECT * FROM users WHERE age LIKE '2_';

-- users 테이블에서 지역 번호가 02인 사람만 조회한다면?
SELECT * FROM users WHERE phone LIKE '02%';

-- users 테이블에서 이름이 '준'으로 끝나는 사람만 조회한다면?
SELECT * FROM users WHERE first_name LIKE '%준';

-- users 테이블에서 중간 번호가 5114인 사람만 조회한다면?
SELECT * FROM users WHERE phone LIKE '%-5114-%';


-- users에서 나이 순으로 오름차순 정렬하여 상위 10개만 조회한다면?
SELECT * FROM users ORDER BY age ASC LIMIT 10;
-- sqlite> SELECT * FROM users ORDER BY age ASC LIMIT 10;
-- first_name  last_name  age  country  phone          balance
-- ----------  ---------  ---  -------  -------------  -------
-- 서영          김          15   제주특별자치도  016-3046-9822  640000
-- 지후          엄          15   경상북도     02-6714-5416   16000
-- 우진          고          15   경상북도     011-3124-1126  300
-- 우진          한          15   강원도      011-8068-4814  3300
-- 은영          이          15   전라남도     010-5284-4904  78000
-- 지훈          김          15   전라북도     02-9385-7954   760
-- 승현          장          15   충청북도     016-5731-8009  450
-- 주원          김          15   전라남도     02-4240-8648   6300
-- 은정          이          15   경상북도     010-6099-6176  5900
-- 정수          강          15   충청북도     02-7245-5623   500

-- 나이 순, 성 순으로 오름차순 정렬하여 상위 10개만 조회한다면?
SELECT * FROM users ORDER BY age, last_name LIMIT 10;
-- sqlite> SELECT * FROM users ORDER BY age, last_name LIMIT 10;
-- first_name  last_name  age  country  phone          balance
-- ----------  ---------  ---  -------  -------------  -------
-- 정수          강          15   충청북도     02-7245-5623   500
-- 우진          고          15   경상북도     011-3124-1126  300
-- 시우          고          15   제주특별자치도  016-3732-8726  270
-- 현숙          곽          15   충청남도     016-7423-1481  710000
-- 서영          김          15   제주특별자치도  016-3046-9822  640000
-- 지훈          김          15   전라북도     02-9385-7954   760
-- 주원          김          15   전라남도     02-4240-8648   6300
-- 예준          김          15   충청남도     02-9726-5034   76000
-- 예준          김          15   충청북도     016-3898-3279  150000
-- 서영          김          15   강원도      010-4016-6803  53000

-- 계좌 잔액 순으로 내림차순 정렬하여 해당 유저의 성과 이름을 10개만 조회한다면?
SELECT last_name, first_name FROM users ORDER BY balance DESC LIMIT 10;
-- sqlite> SELECT last_name, first_name FROM users ORDER BY balance DESC LIMIT 10;
-- last_name  first_name
-- ---------  ----------
-- 김          순옥
-- 우          상철
-- 민          진호
-- 이          재호
-- 강          민준
-- 황          은정
-- 김          영수
-- 허          정남
-- 김          선영
-- 문          미영