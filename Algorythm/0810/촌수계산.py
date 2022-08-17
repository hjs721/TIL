# import sys
# sys.stdin = open('input.txt')

'''
서로 다른 두 사람의 번호
두 사람의 촌수를 나타내는 점수를 출력

9 # 사람의 수(1번~9번, 9명)
7 3 # 촌수를 계산할 두 사람(7번 사람과 3번 사람)
7 # 관계(간선)의 수
1 2
1 3
2 7
2 8
2 9
4 5
4 6
'''

# 인접 리스트!
# 그래프 문제는 정점이 1번부터 시작하는 문제가 많음
# 컴퓨터는 0부터 시작하기 때문에 범위를 n + 1로 설정해준다.
n = int(input())
start, end = list(map(int, input().split()))
m = int(input())
# 빈 리스트를 n + 1개 가진 이차원 리스트
graph = [[] for _ in range(n + 1)]
# pprint(graph) 디버깅

for _ in range(m):
    # 부모 자식 관계
    x, y = list(map(int, input().split()))
    # 무방향(양방향) 인접 그래프 생성
    graph[x].append(y)
    graph[y].append(x)
# pprint(graph)

# 방문처 표시를 할 리스트
visited = [False] * (n + 1)
# dfs를 시작하기 위해 기본값 설정
# stack = [start]
stack = []
stack.append(start, 0)
visited[start] = True

# 정답 출력 변수
answer = -1

# 스택이 비어있지 않을 때까지
while len(stack) != 0:
    # number = 7, 0
    # number = 2, 1
    # numebr = 1
    # numebr = 7? < 이미 방문했음! 빼는 조건문 작성
    # 번호와 촌수를 같이 pop
    number, count = stack.pop()

    # pop한 값이 우리가 원하는 값(end)이면 종료
    if number == end:
        answer = count
        break

    adj_graph = graph[number]

    # 인접하는 값들 탐색
    # graph[numebr] = 2
    # graph[number] = 1, 7, 8, 9
    # graph[number] = 2, 3
    for adj_number in adj_graph[number]:
        # 방문한 적 없을 때만 스택에 값을 append
        # 인접 번호와 촌수를 같이 append
        if not visited[adj_number]:
            stack.append(adj_number, count + 1)
            # 인접 값을 방문 표시
            visited[adj_number] = True

# 그래서 촌수는?
print(answer)