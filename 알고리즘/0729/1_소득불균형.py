import sys

sys.stdin = open("_소득불균형.txt")

T = int(input())
for test_case in range(1, T + 1):
    my_list = [] # 소득 하나씩 넣을 빈 리스트 생성
    N = int(input())
    num = list(map(int, input().split())) # 쪼개서 리스트화
    for i in num:
        if i <= sum(num) // N: # 평균값보다 작거나 같은 수는 전부 리스트에 추가
            my_list.append(i)
    print(f'#{test_case} {len(my_list)}') # 리스트 길이 뽑으면 됨