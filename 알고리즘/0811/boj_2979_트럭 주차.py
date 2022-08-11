import sys
sys.stdin = open('트럭주차.txt')

# 요금
a, b, c = map(int, input().split())
# 트럭
first = list(map(int, input().split()))
second = list(map(int, input().split()))
third = list(map(int, input().split()))
# 가장 마지막에 떠나는 시간
last_out = max(first[1], second[1], third[1])
# 내야할 주차 요금 변수
fee = 0

# 1분부터 마지막 시간까지
for i in range(1, last_out + 1):
    # 트럭 갯수 변수, 기본적으로 0개
    truck = 0
    # 처음 들어온 트럭이 남아있다면 1 추가
    if first[0] < i <= first[1]:
        truck += 1
    # 두번째 들어온 트럭이 남아있다면 1 추가
    if second[0] < i <= second[1]:
        truck += 1
    # 세번째 들어온 트럭이 남아있다면 1 추가
    if third[0] < i <= third[1]:
        truck += 1
    # 요금 계산
    if truck == 1:
        fee += a
    elif truck == 2:
        fee += 2 * b
    elif truck == 3:
        fee += 3 * c
print(fee)