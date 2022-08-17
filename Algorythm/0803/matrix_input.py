# 3x3 크기의 입력을 받아보자
# 1 2 3
# 4 5 6
# 7 8 9

matrix = []
for _ in range(3):
    line = list(map(int, input().split()))
    matrix.append(line)

matrix = [list(map(int, input().split())) for _ in range(3)]

'''
n x m 크기의 입력을 받아보좌
3 4
1 2 3 4
5 6 7 8
9 0 1 2
'''
n = 3
m = 4
matrix = [list(map(int, input().split())) for _ in range(n)]