import sys

sys.stdin = open("_반반.txt")

t = int(input())
for test_case in range(1, t + 1):
    # 인풋값 리스트화해서 정렬
    word = sorted(list(input()))
    # 서로 다른 요소 2개가 2번씩 나오면
    if word[0] == word[1] and word[2] == word[3] and word[0] != word[2]:
        # Yes 출력
        print(f'#{test_case} Yes')
    else:
        # 아니면 No 출력
        print(f'#{test_case} No')

# 좋은 풀이입니다! 좀 더 쉽게 접근하는 방법은 word의 문자에 대해 count()를 사용해 확인하는 방법도 있을 것 같네요!