
# 리스트 메서드 활용 (원본 자체가 변경되고 리턴되는 것은 None)
a = [10, 1, 100]
# 정렬(sort)
new_a = print(a.sort())
print(a, new_a)

# 리스트 sorted 함수 활용 (원본은 그대로, 리턴되는 것이 정렬된 리스트)
b = [10, 1, 100]
# 정렬(sort)
new_b = sorted(b)
print(b, new_b)

# 실제 활용 코드
a.sort()
# a를 정렬된 상태로 활용
b = sorted(b)
# b를 정렬된 상태로 활용


# x의 첫 번째 위치를 반환. 없으면 -1을 반환
'apple'.find('p')
# 1
'apple'.find('k')
# -1

# x의 첫 번째 위치를 반환. 없으면 오류 발생
'apple'.index('p')
# 1
'apple'.index('k')
# error

# 문자열 관련 검증 메소드
'abc'.isalpha() # True
'Ab'.isupper() # False
'ab'.islower() # True
'Title Title!'.istitle() # True

# 문자열 변경
# (old, new, count(숫자))
'coone'.replace('o', 'a')
# caane
'wooooowoo'.replace('o', '!', 2)
# w!!ooowoo

# .strip([chars])
'   와우!\n'.strip()
# '와우!'
'   와우\n'.lstrip()
# '와우!\n'
'   와우\n'.rstrip()
# ' 와우'

# .split(sep = None, maxsplit=-1)
'a, b, c'.split('_')
# ['a,b,c']

# .join([iterable])
# 안에 문자열이 아닌 값이 있으면 typeerror
''.join(['3', '5'])
# 35
names = ','.join(['홍길동', '김철수'])
print(names)
# 홍길동,김철수
numbers = ' '.join(map(str, [10, 20, 100]))
# 10 20 100