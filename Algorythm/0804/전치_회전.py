# 전치 : 행렬의 행과 열을 서로 맞바꿈
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0, 1, 2]
]

transposed_matrix = [[0] * 3 for _ in range(4)]

for i in range(4):
    for j in range(3):
        transposed_matrix[i][j] = matrix[j][i]


# 회전: 90도 180도 270도...