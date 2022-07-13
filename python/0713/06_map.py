numbers = ['1', '2', '3']
# 숫자로 바꿔서 쓰고 싶으면?
# list를 숫자로 형 변환은 불가능합니다. (n = int(numbers)는 불가능)
# 다만, 숫자 형태의 문자(각각)를 변환할 수는 있습니다.

# 이렇게는 가능! 100개, 1000개일 때는?
a = int(numbers[0])
b = int(numbers[1])
c = int(numbers[2])
new_numbers = [a, b, c]

# 반복문!
numbers = ['1', '2', '3']
new_numbers = []
for number in numbers:
    new_numbers.append(int(number)) # append 하나씩 추가함
print(new_numbers)

# map! 모든 반복 가능한 것에 내가 반복하고 싶은 함수를 정함
numbers = ['1', '2', '3']
new_numbers_2 = map(int, numbers)
print(new_numbers_2, type(new_numbers_2))  # <map object at 0x000001F7F41D5FA0> : 이미 함수가 모두 적용된 상태
print(list(new_numbers))  # list로 형변환 (편하게 보기위해 한 것. 반드시 해야하는 것 아님)
# <class 'map'>


# 리스트로 형변환해서 보면 바뀌어있다~!
# 보기 위해서 바꾼 것일 뿐! 반드시 list로 바꿔야하는 것은 아닙니다.