n = int(input()) # 우유가게 수
milk = list(map(int, input().split())) # 우유가게 정보 0 1 2
result = 0 # 먹을 수 있는 우유 수
for i in range(n): # n개 가게 중에서
    if milk[i] == result % 3:
        result += 1 # 0 1 2 순서대로 나올때마다 추가
print(result)