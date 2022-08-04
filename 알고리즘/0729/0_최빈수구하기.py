import sys

sys.stdin = open("_최빈수구하기.txt")

T = int(input())
for test_case in range(1, T + 1):
    num = int(input()) # 테스트 케이스
    score = list(map(int, input().split())) # 점수 리스트로 모으기
    result = 0 # 최빈값
    dict_ = {} # 점수:횟수로 딕셔너리 만들거임
    for i in score: # 점수 리스트 안에서
        if i in dict_: # 키값 i로 점수:횟수가 이미 있으면
            dict_[i] += 1 # 횟수(밸유) 1 더하기
        else:
            dict_[i] = 1 # i라는 키값이 없으면 1 할당
    max_ = 0 # 횟수(밸유)랑 비교할 최대값 기본값 0 설정
    for k, v in dict_.items(): # 딕셔너리에서
        if max_ < v: # 최대값보다 큰 밸유가 있으면
            max_ = v # 그걸 최대값에 할당
            result = k # 해당 밸유의 키값이 결과가 됨
        elif max_ == v: # 동일하면
            if result < k: # 더 큰 키값(점수)인지 확인하고
                result = k # 더큰걸 결과에 할당
    print(f'#{num} {result}')