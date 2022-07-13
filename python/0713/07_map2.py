# 직사각형의 넓이를 구하시오.
# 직사각형 세로는 n, 가로는 m
# Input 예시
# 10, 20
n, m = map(int, input().split())
# input() 타입은 항상 str!!! 문자열!
# 문자열.split() : 내가 구분값(기본:띄어쓰기(sep))을 기준으로 쪼개겠다! 반환 결과는 항상 리스트
# 결국 input().split() : 문자열로 받은 것 각각을 공백을 기준으로 리스트로 쪼갰다 => 리스트 ['10', '20']
# 이 식에서 int는 내장함수임 int()
print(n * m)

# 내장함수를 10을 다 더해주는 함수
def plus10(n):
    return n + 10
numbers = [10, 20, 30]
new_numebrs = list(map(plus10, numbers))
print(new_numebrs)

# map(함수 이름, 반복 가능한 것) int도 함수, plus10도 함수
# 이걸 list()로 감싸면 보기좋기 리스트로 출력됨

counts = [1, 2, 3]
result = map(str, numbers)
print(result, type(result))  # <map object at 0x0000018931D15FA0> <class 'map'>
print(list(result))  # ['10', '20', '30'], str이 문자열로 바꿔주는 함수임