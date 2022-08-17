import sys
sys.stdin = open('연속구간.txt')

# 3줄짜리 인풋
for _ in range(3):
    # 문자열로 입력받음
    s = input()
    # 가장 긴 길이
    len_max = 0
    # 같은 숫자가 나온 횟수
    cnt = 1
    for i in range(8):
        # 전과 같으면 +1, 다르면 1로 초기화
        # i와 i+1로 비교하면 인덱스 오류
        if i != 0 and s[i - 1] == s[i]:
            cnt += 1
        else:
            cnt = 1
        # 반복문 돌면서 cnt가 더 크면 max값 교체
        if cnt > len_max:
            len_max = cnt
    print(len_max)