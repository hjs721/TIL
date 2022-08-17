from pprint import pprint

matrix1 = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# 100*100 행렬
matrix = []
for _ in range(100):
    matrix.append([0] * 100)
pprint(matrix)

print([0] * 2) # [0, 0]
print([1] * 2) # [1, 1]

n = 5 # 행(행이 4개)
m = 5 # 열(열이 3개)
matrix_1 = []
for _ in range(n):
    matrix_1.append([0] * m)
# 리스트 컴프리헨션으로 표현하면:
# 리스트 = [조건이 앞, 반복문이 뒤]
matrix_1 = [[0] * m for _ in range(n)]

matrix_2 = [[0] * m] # [[0, 0, 0, 0, 0]] # [00000]을 하나의 원소로 가진 리스트가 나옴
matrix_3 = [[0] * m] * n # n*m 매트릭스 배열이 나옴~!!


# 주의! 리스트 컴프리헨션 vs 리스트 곱셈 연산:
# matrix_1과 matrix_3은 같은가?
# 생김새는 똑같지만 메모리 주소값이 다름
# 원소값을 변경해보면 알 수 있음

matrix_1[0][0] = 1
print(matrix_1)
# [[1, 0]
#  [0, 0]]

matrix_3[0][0] = 1
print(matrix_3)
# [[1, 0]
#  [1, 0]]

# 가능하면 컴프리헨션을 이용하자!