print('hi', 'hello') # 기본값 sep는 ' '로 정의되어있음
print('hi', 'hello', sep='-') # sep 부분이 키워드(첫번째에 못쓰는거). 키워드 이용해서 -로 바꿔준것

def add(x, y=0):  # y=0을 기본값으로 설정, 따로 넣지 않으면 0이 사용됨
    return x + y
print(add(2))

print(1, 2, 3, 4, 5, 6, 7, 8)

# 정해지지 않은 갯수의 인자
def my_add(*numbers):
    # 내부적으로 numebrs가 tuple
    return numbers
result = my_add(1, 2, 3)
print(result, type(result)) # (1, 2, 3) <class 'tuple'>

def my_func(**kwargs):
    return kwargs
result = my_func(name='홍길동', age='100', gender='M')
print(result, type(result)) # {'name': '홍길동', 'age': '100', 'gender': 'M'} <class 'dict'>