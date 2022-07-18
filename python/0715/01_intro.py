import random

# numbers = random.sample([1, 2, 3], 2)
# print(numbers, type(numbers))

# 1~45까지의 숫자!
# 그 중에 6개
n = int(input('얼마 쓸래? '))
for i in range(n):
    numbers = random.sample(range(1, 46), 6)
    numbers.sort()
    print(numbers)
