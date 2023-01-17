N = input()
num = N
cnt = 0
while True:
    if len(num) == 1:
        num = "0" + num
    sum_ = str(int(num[0]) + int(num[1]))
    num = num[1] + sum_[-1]
    cnt += 1
    if N == num:
        break
print(cnt)
# 시간초과...


N = int(input())
num = N
cnt = 0
while True:
    a = num // 10
    b = num % 10
    c = (a + b) % 10
    num = b * 10 + c
    cnt += 1
    if num == N:
        break
print(cnt)
