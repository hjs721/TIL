N = int(input())
list_ = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    grade = 1
    for j in range(N):
        if list_[i][0] < list_[j][0] and list_[i][1] < list_[j][1]:
            grade += 1
    print(grade, end=' ')