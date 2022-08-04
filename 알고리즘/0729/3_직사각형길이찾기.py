import sys

sys.stdin = open("_직사각형길이찾기.txt")


T = int(input())
for test_case in range(1, T + 1):
    a, b, c = map(int, input().split())
    # 직사각형은 마주보는 두 변의 길이가 같다. 짝이 없는 하나를 출력하면 됨
    if a == b:
        answer = c
    elif b == c:
        answer = a
    elif c == a:
        answer = b
    print(f'#{test_case} {answer}')