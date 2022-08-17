import sys

sys.stdin = open("_신용카드만들기1.txt")

T = int(input())
for test_case in range(1, T + 1):
    nums = list(map(int, input().split()))
    for i in range(len(nums)): # 받은 숫자들 중에서
        if i % 2 == 0: # 홀수자리(인덱스는 짝수) 값들만
            nums[i] = nums[i] * 2 # 2배 시켜주고 더한다(sum)
    result = 10 - sum(nums) % 10 # N이 들어가는 총합이 10의 배수여야 함
    if result == 10: # 10을 0으로 바꿈
        result = 0
    print(f'#{test_case} {result}')