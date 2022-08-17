'''
오목은 델타서치로 풀어야 됨 (범위 5개??)
5개 놓이면 이김. 6목은 이긴 것이 아닌 걸로
N : 가로세로 길이가 19
검은 바둑알 1, 흰 바둑알 2, 빈자리 0 각각 한칸씩 띄어서 입력됨
가장 왼쪽에 있거나 가장 위에 있는 바둑돌 출력

보통의 델타탐색은 상하좌우로 탐색하지만
이 문제에서는 우, 하, 우하, 우상으로 탐색

델타_y = [0, 1, 1, -1]
델타_x = [1, 0, 1, 1]

while True:
    # 조건1. 범위를 벗어나면 안된다. 범위 벗어나면 break
    # 조건2. 같은 색 돌이 나와야 함. 다른색 나오면 break로 탈출
    # 같은 색 돌 변수에 + 1
    # 다음 좌표 탐색 : +1이 아니고 +델타값으로 가야됨
'''
from pprint import pprint

# 우 하 우상 우하
dy = [0, 1, -1, 1]
dx = [1, 0, 1, 1]
Black = 1
White = 2
N = 19

board = []

answer = 0

# 오목판 상황 입력
for _ in range(N):
    # 하나이ㅡ 행을 입력
    temp_list = list(map(int, input().split()))
    board.append(temp_list)

# 이중 반복문
for y in range(N):
    for x in range(N):
        # 검은돌이나 흰돌일때만 델타 탐색 수행
        if board[y][x] == Black or board[y][x] == White:
            # 델타 탐색
            for d in range(4):
                # 방향이 바뀔 때마다 돌의 개수가 갱신(0으로)
                stone_count = 0
                # 다음 좌표 탐색
                ny = y + dy[d]
                nx = x + dx[d]

                while True:
                    # 인덱스 조건
                    if -1 < ny < N and -1 < nx < N:
                        break
                    # 같은색(값)돌인지 확인
                    if board[y][x] != board[ny][nx]:
                        break

                    # 같은 값이고 범위를 벗어나지 않으면
                    stone_count += 1

                    # 같은 방향 다음 좌표 탐색
                    ny = ny + dy[d]
                    nx = nx + dx[d]

                # 돌의 개수가 5개라면
                if stone_count == 5:
                    # 이전 좌표
                    prev_y = y - dy[d]
                    prev_x = x - dx[d]
                    # 육목인지 판단
                    # 조건1. 이전좌표가 범위를 벗어나면 오목이다
                    # if not (-1 < ny < N and -1 < nx < N):
                    # 기준 좌표의 값과 이전 좌표의 값이 다르면 오목
                    # if board[y][x] != board[prev_y][prev_x]:

                    # 조건 1과 조건 2를 만족하면 오목 완성
                    if not (-1 < ny < N and -1 < nx < N) or board[y][x] != board[prev_y][prev_x]:
                        # 무승부가 아니라면 answer 값 갱신
                        answer = board[y][x]
                        # 현재 돌의 색 출력
                        print(board[y][x])
                        # 현재 돌의 좌표 출력
                        print(y + 1, x + 1)

# 전체를 반복했는데 무승부다:
if answer == 0:
    print(answer)