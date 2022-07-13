# 정의
# 1. def
# 2. 함수 이름 : add
# 3. Input : a, b
def add(a, b):
    # return : 값을 반환
    return a + b
# 호출
print(add(5, 10))

def minus(a, b):
    return a - b
print(minus(10, 5))

# 내장 함수 호출
print(sum([1 ,2, 3]))

# 예시 # result부터 거꾸로 보기!!
num1 = 0
num2 = 1

def func1(a, b):
    return a + b

def func2(a, b):
    return a - b

def func3(a, b):
    return func1(a, 5) + func2(5, b)  # 5 + 4

result = func3(num1, num2) # (0, 1)
print(result) # 9

def foo():
    return 1, 2

result = foo()
print(result, type(result)) # tuple # 함수는 하나만 반환함. 컴마로 이어주면 하나의 tuple 값을 반환

def no():
    a = 1

result = no()
print(result, type(result)) # None <class 'Nonetype'>   # print 함수는 None

a = print('Hi')
print(a, type(a)) # None <class 'NoneType'>
# print 함수는 출력을 해주고 return 값은 없습니다...(None)

a = 'hi'
print(a)