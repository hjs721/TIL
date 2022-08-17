n, m = map(int, input().split())
matrix = [list(input()) for _ in range(n)]

x = 0
y = 0 # X가 하나도 없다고 기본값 설정

for i in range(n): # 행 중에서
    if 'X' not in matrix[i]: # X가 하나도 없는 행의 갯수 세기
        x += 1
for j in range(m): # 열 인덱스 고정하고 행 인덱스 돌면 됨 # 그럴려면 n 반복
    if 'X' not in [matrix[i][j] for i in range(n)]: # 컴프리헨션 형태로 if문 안에도 반복문 넣을 수 있음
        y += 1
print(max(x, y)) # 둘 중에 더 큰 값 출력