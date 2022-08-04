n = int(input())
num = [[], [], []]
for _ in range(n):
    a, b, c = map(int, input().split())
    num[0].append(a)
    num[1].append(b)
    num[2].append(c) # 행, 열이 아니라 열, 행으로 매트릭스를 만들어야 함

score = [0] * n # 정답 리스트 설정
for i in range(3): # 행 고정
    for j in range(n): # 열 이동
        if num[i].count(num[i][j]) == 1: # 같은 점수가 존재하지 않으면 # 카운트메서드 : 특정 값이 몇개인지 알려줌
            score[j] += num[i][j] # 점수 더해줌
for s in score: # 점수합 순서대로 출력
    print(s)



# 코드리뷰
from pprint import pprint

list_ = [[100, 99, 98],
[100, 97, 92],
[63, 89, 63],
[99, 99, 99],
[89, 97, 98]
]
# pprint(list_)
col_list = []
# 리스트를 90도 회전
for x in range(3):
    col = []
    for y in range(5):
        col.append(list_[x][y])

    col_list.append(col)

score_list = [0] * 5
for x in range(3):
    col = col_list[x]
    for y in range(5):
        # 친구의 점수
        score = col[y]
        # 친구의 점수가 리스트에서 1개일 때
        if col.count(score) ==1:
            # 점수 증가
            score_list[y] += score
pprint(score_list)