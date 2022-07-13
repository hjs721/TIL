def minus_and_product(x, y):
    return x - y, x *y
print(minus_and_product(4,5))

def foo():
    return 1, 2
result = foo()
print(result, type(result)) # tuple로 묶어서 반환 # (1, 2) <class 'tuple'>

def no():
    a = 1
result = no()
print(result, type(result)) # None <class 'NoneType'> # 어떤 결과도 반환하지 않음