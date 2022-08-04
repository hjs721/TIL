a, b = map(int,input().split()) # 3 7
data = [] # 범위 지정해서 합 구할 리스트
N = 1 # 1, 2, 2, 3, ..이니까 시작점 1

# for문은 명확한 범위가 필요
while len(data) <= b:
    for i in range(N):
        data.append(N)
    N += 1
# print(data)
print(sum(data[a - 1 : b]))