print(
    """문자열 안에 '작은 따옴표'나 "큰 따옴표"를 사용할 수 있고
여러 줄을 사용할 때도 편리하다"""
)

a = 5  # 숫자형 int
b = "5"  # 문자형 str
print(a, b)
print(a, type(a))
print(b, type(b))

# 길이
fruit = "apple"
print(len(fruit))  # 5

# 접근
# fruit 변수는 값이 'apple'
# 컴퓨터에서는 숫자를 0부터
print(fruit[1])  # p

# 슬라이싱
print(fruit[1:3])
# 인덱스 1 이상, 3 미만
# a p p l e
# 0 1 2 3 4

# 마지막 값은?
print(fruit[len(fruit) - 1])
print(fruit[-1])  # e

# 스텝을 줄수도 있음
alpha = "abcdefghi"
print(alpha[2:5:2])  # 인덱스 2 이상 5 미만을 한칸씩 띄워서 # ce

print(alpha[:3])  # 0:3 # abc
print(alpha[5:])  # 5:마지막인덱스 # fghi

print(alpha[::])  # 그대로
print(alpha[::-1])  # 거꾸로

# 결합(Concatenation)
"hello" + "python!"

# 반복(Repetition)
"hi!" * 3

# 포함(Membership)
"a" in "apple"  # True
"app" in "apple"  # True
"b" in "apple"  # False
