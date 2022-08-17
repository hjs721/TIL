SELECT COUNT(*) FROM healthcare;
-- COUNT(*)
-- --------
-- 1000000

SELECT COUNT(*) FROM healthcare WHERE 10 > age;
-- COUNT(*)
-- --------
-- 156277

SELECT COUNT(*) FROM healthcare WHERE gender = 1;
-- COUNT(*)
-- --------
-- 510689

SELECT COUNT(*) FROM healthcare WHERE smoking = 3 AND is_drinking = 1;
-- COUNT(*)
-- --------
-- 150361

SELECT COUNT(*) FROM healthcare WHERE va_left >= 2.0 AND va_right >= 2.0;
-- COUNT(*)
-- --------
-- 2614

SELECT DISTINCT sido FROM healthcare;
-- sido
-- ----
-- 36
-- 27
-- 11
-- 31
-- 41
-- 44
-- 48
-- 30
-- 42
-- 43
-- 46
-- 28
-- 26
-- 47
-- 45
-- 29
-- 49

SELECT id FROM healthcare WHERE waist > 40 AND WEIGHT < 40;