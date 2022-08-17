from pprint import pprint

# 정점 갯수, 간선 갯수
n, m = map(int, input().split())

# 행렬 초기화
graph = [[0] * (n + 1) for _ in range(n + 1)]
# 리스트 초기화
graph2 = [[] for _ in range(n + 1)]

for _ in range(m):
    # 간선의 양 끝점(서로 연결되어 있음)
    v1, v2 = map(int, input().split())
    # 빈 행렬에 인풋값 위치 받아서 1로 넣어주기
    # 무방향이므로 인자값 바꿔서도 실행
    graph[v1][v2] = 1
    graph[v2][v1] = 1
    # 빈 리스트에도 같은 방법으로 실행
    graph2[v1].append(v2)
pprint(graph)
print(graph2)