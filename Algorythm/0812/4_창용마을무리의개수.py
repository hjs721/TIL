import sys

sys.stdin = open("_창용마을무리의개수.txt")


t = int(input())
for test_case in range(1, t + 1):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        v1, v2 = list(map(int, input().split()))
        graph[v1].append(v2)
        graph[v2].append(v1)

# dfs로 풀어야 한다는 건 알겠는데 어떻게?ㅠㅠ
# 시작점 설정
start = v1
# False 리스트 만들어두고
visited = [[False] * (n + 1)]
# 방문한 지점은 True로 바꿔주기
# 시작점은 방문했으니까 이미 True
visited[start] = True
# 빈 스택에도 시작점 채워두기
stack = []
stack.append(start)
stack = [start]

# 스택이 비어있지 않을 때까지 반복
while len(stack) != 0:
    # 팝으로 노드 뽑기
    number = stack.pop()
    # 뽑은 노드를 그래프에 넣어서 연결된 모든 좌표 확인
    for adj in graph[number]:
        # 아직 방문하지 않은 새 노드라면
        if not visited[adj]:
            # 방문한 노드 True 표시하고
            visited[adj] = True
            # 스택에 쌓기
            stack.append(adj)
        # 이미 방문한 노드는 더 탐색 안하고 건너뛰기
        else:
            continue
        # 모르겠다...


'''
우선 코드는 tc를 도는 for 문안에 작성해 주셔야 합니다!
29번째 줄부터 작성하신 dfs는 잘 작성해 주셨습니다. 풀이 방법에 대해 말씀드리자면 모든 주민들에 대해 for 문을 돌면서 visited가 체크되지 않았다면 이 주민을 시작으로 dfs를 진행해 서로 알고 있는 사람들을 체크해 주시면 됩니다.
다른 튜터 분의 코드를 첨부해 드릴 테니 한번 읽어보시고 생각해 보시면 좋을 것 같습니다

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int,input().split())
    adj_list = [[] for _ in range(N+1)]
    for _ in range(M):
        x, y = map(int,input().split())
        adj_list[x].append(y)
        adj_list[y].append(x)
    
    visited = [0]*(N+1)
    answer = 0
    for node in range(1, N+1):
        if visited[node] != 0:
            continue
        stack = [node]
        visited[node] = 1
        answer += 1
        while stack:
            cur = stack.pop()
            for nxt in adj_list[cur]:
                if visited[nxt]==0:
                    visited[nxt] = 1
                    stack.append(nxt)
    
    print(f'#{test_case} {answer}')
'''