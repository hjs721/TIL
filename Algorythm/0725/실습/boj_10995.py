# https://www.acmicpc.net/problem/10995
# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

# 출력
# 첫째 줄부터 차례대로 별을 출력한다.

N = int(input())
a = '* '
for i in range(1, N + 1):
    if i % 2 == 0:
        answer = ' '
    else:
        answer = ''
    print(answer, a*N, sep = '')