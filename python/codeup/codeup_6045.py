# 정수 3개를 입력받아 합과 평균을 출력해보자.

a, b, c = map(int, input().split())
d = format(((a + b + c) / 3), '.2f')
print(a + b + c, d)