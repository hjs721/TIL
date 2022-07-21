# 동적 타입 언어인 파이썬에서...
# 정적 타입으로 바꿔주는 것이 아니라!!
# 그냥 힌트... 그냥 노트... 주석같은 느낌임
# 변수 어노테이션
a : int = 3
print(a)
# 3
# 실행됨!

# 함수 어노테이션
def add(x: int, y: int) -> int:  # int로 쓰라는 힌트만 주는 것. str로 써도 출력은 됨
    return x + y
print(add(7, 4))
print(add('hi', 'hello'))
# 아래 함수와 완전히 동일
def add2(x, y):
    return x + y
print(add2(7, 4))