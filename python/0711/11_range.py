numbers = range(5)
print(numbers)  # range(0, 5)
# 숫자를 확인하려면 리스트 변환해서 보면 편함
print(list(numbers))  # [0, 1, 2, 3, 4]

print(list(range(3)))  # [0, 1, 2]
print(list(range(1, 5)))  # [1, 2, 3, 4]
print(list(range(1, 5, 2)))  # [1, 3]
print(list(range(6, 1, -1)))  # [6, 5, 4, 3, 2]
print(list(range(6, 1, 1)))  # []
