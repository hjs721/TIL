# 런타임에러남
n, m = map(int, input().split())
arr = [list(map(int ,input().split())) for _ in range(n)]
k = int(input())
coor = [list(map(int ,input().split())) for _ in range(k)]

for i in coor:
    sum_ = 0
    for j in range(i - 1, x):
        for k in range(j - 1, y):
            sum_ += arr[j][k]
    print(sum_)



# 코드리뷰
n, m = map(int, input().split())
list_ = [list(map(int ,input().split())) for _ in range(n)]
k = int(input())

for _ in range(k):
    i, j, x, y = map(int, input().split())

    i -= 1
    j -= 1
    x -= 1
    y -= 1

    sum_ = 0
    # 이중 반복문
    # i -> x
    for r in range(i, x + 1):
        # j -> y
        for c in range(j, y + 1):
            sum_ += list_[r][c]

    print(sum_)