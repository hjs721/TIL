from pprint import pprint

n, m = map(int, input().split())

# 행렬 초기화
graph = [[0] * (n + 1) for _ in range(n + 1)] # 1~6까지니까 n + 1 넣어줘야
graph2 = [[] for _ in range(n + 1)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1][v2] = 1
    graph2[v1].append(v2)

pprint(graph)
print(graph2)