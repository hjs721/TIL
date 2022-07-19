# 주어진 숫자부터 0까지 순서대로 찍어보세요
# input 8

a = int(input())
for i in range(a, -1, -1):
    print(i, end=' ')

for i in range(0, a + 1):
    print(a - i, end=' ')