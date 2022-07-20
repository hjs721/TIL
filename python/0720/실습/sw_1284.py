import sys
sys.stdin = open("input.txt", "r")

# A사 : W * P
# B사 :
#   R 이하 : Q
#   R 초과 : Q + S*(W-R)

T = int(input()) # 2
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    A = W * P
    if R > W:
        B = Q
    else:
        B = Q + S*(W-R)
    print(f'{test_case} {min(A, B)}') # 최솟값 내장함수 min()