# 369게임
# 369 박수를 -로 대체, 369갯수만큼 박수(-)
# 1 2 - 4 5 - 7 8 - 10 11 12 - ... 29 - - -- -...

N = int(input())
for i in range(1, N + 1): # 1부터 N 중에서
    I = str(i) # 숫자 하나하나 뜯을 수 있게 문자열로 형변환
    count = 0 # 조건에 맞으면 - 갯수 추가
    for num in I: # 숫자 중에 하나라도
        if num in '369': # 369 중 하나라면
            count += 1 # - 갯수 하나씩 추가 # 아니면 말고라서 else 필요없음
    if count == 0: # 369가 없으면
        print(I, end = ' ') # 문자열 그대로 출력
    else: # 하나라도 있으면
        print('-' * count, end = ' ') # 갯수대로 - 출력