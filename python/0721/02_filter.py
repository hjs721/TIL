# 3의 배수인 리스트로만 만들기

numbers = [1, 2, 5, 10, 3, 9, 12]
# 기본 반복/조건 코드
result = []
for n in numbers:
    if n % 3 == 0:
        result.append(n)
print(result)

# 람다 활용
print(filter(lambda n: n%3==0, numbers))
# [3, 9, 12]
# <filter object at 0x000001EECDB35FA0>

print(list(filter(lambda n: n%3==0, numbers)))
# [3, 9, 12]
# [3, 9, 12]

# 함수 활용
def is_3(n):
    return n % 3 == 0
print(list(filter(is_3, numbers))) # filter(함수, 반복가능한 것)