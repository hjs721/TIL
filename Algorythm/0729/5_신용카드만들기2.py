import sys

sys.stdin = open("_신용카드만들기2.txt")

T = int(input())
for test_case in range(1, T + 1):
    word = input() # 문자열로 인풋 받기
    nums = [] # - 제외한 숫자들로 리스트 생성
    for i in word:
        if i != '-': # -가 아닌 요소는
            nums.append(i) # 전부 리스트에 추가
    nums = list(map(int, nums)) # 문자열로 받은걸 정수형으로 형변환
    if len(nums) == 16: # 숫자 총 갯수가 16개일 때
        if nums[0] == 3 or nums[0] == 4 or nums[0] == 5 or nums[0] == 6 or nums[0] == 9: # 시작 숫자가 34569 라면
            answer = 1
        else: # 시작 숫자가 다른 숫자라면
            answer = 0
    else: # 갯수가 16개가 아닐 때
        answer = 0
    print(f'#{test_case} {answer}')