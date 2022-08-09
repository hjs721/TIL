r, c = map(int, input().split())
matrix = [list(input().split()) for _ in range(r)]

델타x = [0, 1, 0, 1]
델타y = [0, 0, 1, 1] # 2행 2열 델타탐색

result = [0] * 5

def locate(x, y):
    # 부숴야하는 차의 갯수
    cnt = 0

    for dx, dy in (0, 0), (1, 0), (0, 1), (1, 1):
        if matrix[x + dx][y + dy] == '#':
            return -1
        elif matrix[x + dx][y + dy] == 'X':
            cnt += 1
    return cnt