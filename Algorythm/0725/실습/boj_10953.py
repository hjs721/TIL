T = int(input()) # 5
for test_case in range(1, T + 1):
    A, B = map(int, input().split(',')) # 뭘로 나눌지 split() 안에 넣기
    print(A + B)