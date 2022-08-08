n = int(input())
num = 0 # 몇번째 나타내는 변수
num_6 = 666

# 범위제한없이 무한반복해야 하니까 while문
# 666이 1, 숫자 올려가면서 666 한번 더 나올때마다 num 변수에 1씩 추가헤주면 됨
# n에 도달하면 종료
while True:
    if '666' in str(num_6):
        num += 1
    if num == n:
        print(num_6)
        break
    num_6 += 1