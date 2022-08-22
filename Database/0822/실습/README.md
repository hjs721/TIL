### 1. playlist_track 테이블에 `A`라는 별칭을 부여하고 데이터를 출력하세요.
| 단, 모든 컬럼을 `PlaylistId` 기준으로 내림차순으로 5개만 출력하세요.
```sql
SELECT * FROM playlist_track A ORDER BY PlaylistID DESC LIMIT 5;
```

```bash
PlaylistId  TrackId
----------  -------
18          597
17          3290
17          2096
17          2095
17          2094
```



### 2. tracks 테이블에 `B`라는 별칭을 부여하고 데이터를 출력하세요

| 단, 모든 컬럼을 `TrackId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
SELECT * FROM tracks B ORDER BY TrackID LIMIT 5;
```



### 3. 각 playlist_track 해당하는 track 데이터를 함께 출력하세요.

| 단, PlaylistId, Name 컬럼을 `PlaylistId` 기준으로 내림차순으로 10개만 출력하세요. 
```sql
SELECT PlaylistID, Name
FROM playlist_track JOIN tracks
    ON playlist_track.TrackID = tracks.TrackID
ORDER BY PlaylistID DESC LIMIT 10;
```

```bash
PlaylistId  Name
----------  -----------------------
18          Now's The Time
17          The Zoo
17          Flying High Again
17          Crazy Train
17          I Don't Know
17          Looks That Kill
17          Live To Win
17          Ace Of Spades
17          Creeping Death
17          For Whom The Bell Tolls
```



### 4. `PlaylistId`가 `10`인 track 데이터를 함께 출력하세요. 

| 단, PlaylistId, Name 컬럼을 `Name` 기준으로 내림차순으로 5개만 출력하세요.
```sql
SELECT PlaylistID, Name
FROM playlist_track JOIN tracks
    ON playlist_track.TrackID = tracks.TrackID
ORDER BY Name DESC LIMIT 5;
```

```bash
PlaylistId  Name
----------  -------------------
1           Ultimo Pau-De-Arara
8           Ultimo Pau-De-Arara
1           Oia Eu Aqui De Novo
8           Oia Eu Aqui De Novo
1           Oculos
```



### 5. tracks 테이블을 기준으로 tracks `Composer` 와 artists 테이블의 `Name`을 `INNER JOIN`해서 데이터를 출력하세요.

| 단, 행의 개수만 출력하세요.
```sql
SELECT COUNT(*)
FROM tracks JOIN artists
    ON tracks.Composer = artists.Name;
```

```bash
COUNT(*)
--------
402
```



### 6. tracks 테이블을 기준으로 tracks `Composer` 와 artists 테이블의 `Name`을 `LEFT JOIN`해서 데이터를 출력하세요.

| 단, 행의 개수만 출력하세요.
```sql
SELECT COUNT(*)
FROM tracks LEFT OUTER JOIN artists
    ON tracks.Composer = artists.Name;
```

```bash
COUNT(*)
--------
3503
```



### 7. `INNER JOIN` 과 `LEFT JOIN` 행의 개수가 다른 이유를 작성하세요.

```plain
INNER JOIN은 두 테이블의 교집합, 즉 칼럼 값이 동일한 행만 불러오지만 LEFT JOIN은 동일한 값이 없는 행도 불러온다. LEFT이기 때문에 먼저 나온 테이블이 기준이 된다.
```



### 8. invoice_items 테이블의 데이터를 출력하세요.

| 단, InvoiceLineId, InvoiceId 컬럼을 `InvoiceId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
SELECT InvoiceLineID, InvoiceId FROM invoice_items ORDER BY InvoiceID LIMIT 5;
```

```bash
InvoiceLineId  InvoiceId
-------------  ---------
1              1
2              1
3              2
4              2
5              2
```



### 9. invoices 테이블의 데이터를 출력하세요.

| 단, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
SELECT InvoiceID, CustomerID FROM invoices ORDER BY InvoiceID LIMIT 5;
```

```bash
InvoiceId  CustomerId
---------  ----------
1          2
2          4
3          8
4          14
5          23
```



### 10. 각 invoices_item에 해당하는 invoice 데이터를 함께 출력하세요.

| 단, InvoiceLineId, InvoiceId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.
```sqlite
SELECT InvoiceLineId, invoices.InvoiceId
FROM invoice_items JOIN invoices
    ON invoice_items.invoiceId = invoices.InvoiceId
ORDER BY invoices.InvoiceId DESC LIMIT 5;
```

```bash
InvoiceLineId  InvoiceId
-------------  ---------
2240           412
2226           411
2227           411
2228           411
2229           411
```



### 11. 각 invoice에 해당하는 customer 데이터를 함께 출력하세요.

| 단, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.
```sqlite
SELECT InvoiceID, customers.CustomerID
FROM invoices JOIN customers
    ON invoices.CustomerID = customers.CustomerID
ORDER BY InvoiceID DESC LIMIT 5;
```

```bash
InvoiceId  CustomerId
---------  ----------
412        58
411        44
410        35
409        29
408        25
```



### 12. 각 invoices_item(상품)을 포함하는 invoice(송장)와 해당 invoice를 받을 customer(고객) 데이터를 모두 함께 출력하세요.

| 단, InvoiceLineId, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.
```sqlite
SELECT invoice_items.InvoiceLineId, invoice_items.InvoiceId, customers.CustomerId 
FROM invoice_items JOIN invoices
    ON invoice_items.InvoiceId = invoices.InvoiceID
JOIN customers
    ON invoices.CustomerID = customers.CustomerID
ORDER BY invoice_items.InvoiceID DESC LIMIT 5;
```

```bash
InvoiceLineId  InvoiceId  CustomerId
-------------  ---------  ----------
2240           412        58
2239           411        44
2238           411        44
2237           411        44
2236           411        44
```



### 13. 각 cusotmer가 주문한 invoices_item의 개수를 출력하세요.

| 단, CustomerId와 개수 컬럼을 `CustomerId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
SELECT invoices.CustomerId, COUNT(*)
FROM invoice_items JOIN invoices
    ON invoice_items.InvoiceId = invoices.InvoiceId
GROUP BY invoices.CustomerId
ORDER BY invoices.CustomerId
LIMIT 5;
```

```bash
CustomerId  COUNT(*)
----------  --------
1           38
2           38
3           38
4           38
5           38
```

