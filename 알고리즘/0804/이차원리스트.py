'''
IM : intermediate
index manipulation. 인덱스 조작만 잘하면 코테짱될수도

그래프 -> 인접행렬
'''

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 0, 1, 2]
]

# n x m
n = len(matrix)
m = len(matrix[0])

# 행 우선 순회
for r in range(n):
    for c in range(m):
        print(matrix[r][c], end = ' ')

# 열 우선 순회
for i in range(m):
    for j in range(n):
        print(matrix[j][i], end = ' ')
    print()
'''
1 5 9
2 6 0
3 7 1
4 8 2
'''

# 인자 다 더해보기
total = 0
for row in matrix:
    # for elem in row:
    #     total += elem
    total += sum(row) # 반복문 두번 중첩 : O(n제곱)
print(total)

# 맵 이용해서 해보기 (행우선)
total = sum(map(sum, matrix)) # 짧긴한데 시간복잡도 똑같음
print(total)

# 함수 정의해놓으면
def matrix_sum(matrix):
    return sum(map(sum, matrix))
print(matrix_sum(matrix)) # 시간복잡도 n제곱 똑같음

# 열우선 인자합은... 돌아야 됨...


# 행우선 순회를 이용해 이차원 리스트의 최대값, 최소값 구하기
# 최대값
matrix = [
    [0, 5, 3, 1],
    [4, 6, 10, 8],
    [0, -1, 1, 5]
]

max_value = 0

for i in range(3):
    for j in range(4):
        if matrix[i][j] > max_value:
            max_value = matrix[i][j]
print(max_value)
# map으로
max_value = max(map(max, matrix))

# 최소값
min_value = 9999999

for i in range(3):
    for j in range(4):
        if matrix[i][j] < min_value:
            min_value = matrix[i][j]
print(min_value)
# map으로
min_value = min(map(min, matrix))