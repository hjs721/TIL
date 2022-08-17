'''
dfs/델타 문제
델타 탐색 : 4방향(대각선은 필요 없으니까)
델타 리스트를 작성해보자!

행 갯수 : 1차원 리스트의 갯수
열 갯수 : 1차원 리스트에서 요소의 갯수

예시는 총 4개의 그림 / 가장 넓은 넓이는 9

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# 세로 가로 입력
# 공백을 기준으로 나뉘어진 숫자 2개
n, m = list(map(int, input().split()))

# n개의 리스트를 가진 2차원 리스트 입력
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# dfs에서 가장 중요한 파트 : 방문처리!! 한 사이클 돌릴때마다 카운트 +1
# dfs는 한방향으로만 감
visited = []
# 행의 갯수만큼 리스트 생성
for _ in range(n):
    # 열의 갯수만큼 그래프 생성
    visited_list = [False] * m
    visited.append(visited_list)

# 방문 안하고, 값이 1인 것을 세어주면 됨
'''
# 상하좌우 탐색 델타 리스트
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# 가로 세로의 크기를 입력
# 두 숫자가 공백으로 구분
n, m = list(map(int, input().split()))

# 이차원 그래프를 생성
# 빈 그래프 생성
graph = []
# n번만큼 일차원 그래프를 입력받고 추가
for _ in range(n):
    graph_list = list(map(int, input().split()))
    graph.append(graph_list)

# 방문 표시 이차원 그래프
visited = []
# n번 만큼의 일차원 그래프를 추가
for _ in range(n):
    # 불리언(False)가 m개인 일차원 그래프?
    visited_list = [False] * m
    visited.append(visited_list)

painting = 0
painting_size_list = []

# 모든 좌표에서 dfs 로직 실행
# 이차원 리스트를 순회할 이중 반복문
for sy in range(n):
    for sx in range(m):
        # (sy, sx) 값이 1이고, 방문하지 않았다면
        if not visited[sy][sx] and graph[sy][sx] == 1:
            # dfs 실행
            stack = []
            # 시작점을 스택에 append
            stack.append([sy, sx])
            # 시작점을 방문처ㅣㄹ
            visited[sy][sx] = True

            # 그림의 갯수 +1
            painting += 1

            # 그림 넓이?
            painting_size = 0

            # dfs
            # 스택이 비어있지 않으면 반복한다
            # while stack:
            while len(stack) != 0:
                y, x = stack.pop()
                # 그림의 넓이
                painting_size += 1

                # 델타 탐색 시행
                for d in range(4):
                    ny = y + dy[d]
                    nx = x + dx[d]

                    # 조건 1. 범위 설정
                    if not (-1 < ny < n and -1 < nx < m):
                        continue
                    # 조건 2. 방문 확인
                    # 방문했던 좌표라면 코드 실행 x
                    if visited[ny][nx] == True:
                        continue
                    # 조건 3. 좌표 값이 1이어야 함
                    if graph[ny][nx] != 1:
                        continue

                    # 조건을 다 통과하면 stack에 다음 좌표를 넣고 방문처리
                    stack.append((ny, nx))
                    visited[ny][nx] = True

            painting_size_list.append(painting_size)

if len(painting_size_list) != 0:
    print(painting)
    print(max(painting_size_list))
else:
    print(0)
    print(0)