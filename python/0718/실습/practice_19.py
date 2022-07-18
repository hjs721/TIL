# 문제 19. 숫자의 길이 구하기
number = 123

# 1. 문자열로 바꿔서 구하기
print(len(str(number)))

# 2. 123 몫으로 while
result = 0
# 몫이 0이 되면 종료해야 하니까 0이 아닐 때까지
# int는 0이 아닌 다른 수면 무조건 True
# 0이면 False니까 그냥 넘버만 적어도 됨
while number != 0:
    number = number // 10
    result += 1
print(result)
# 이렇게 줄일 수도 있음
while number:
    number //= 10
    result += 1
print(result)

# 3. log
number = 123456
import math
print(int(math.log(number, 10)) + 1)