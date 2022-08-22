-- 여기에 해당하는것만
SELECT *
FROM albums JOIN artists
    ON albums.Artistid = artists.Artistid
LIMIT 5;

-- 앨범즈에 아티스트를 붙여서
SELECT *
FROM albums LEFT JOIN artists
    ON albums.Artistid = artists.Artistid
LIMIT 10;