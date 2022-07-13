print('''문자열 안에 '작은 따옴표'나
"큰 따옴표"를 사용할 수 있고
여러 줄을 사용할 때도 편리하다.''')


a = 5 # int
b = '5' # str
print(a, type(a))
print(b, type(b))


# 길이 - lenth
fruit = 'abcde'
print(len(fruit)) # 5


# 접근/인덱싱 # fruit 변수의 값이 abcde
# 컴퓨터에서는 숫자를 0부터
print(fruit[1]) # b


# 슬라이싱
print(fruit[1:3]) # bc
# 인덱스 1이상, 3미만
# a b c d e
# 0 1 2 3 4
print(fruit[2:5]) #cde
# 2이상 5미만


# 마지막 값은?? # 길이(5) - 1
# 파이썬은 음의 인덱스도 가지고 있다!
print(fruit[len(fruit)-1])
print(fruit[-1])


# abcdefg
# s[2:5:2] : ce 여기서 2는 step
# s[2:5:-1] : fed 여기서 -1은 step
# s[::] : 처음부터 끝까지 1씩 == s[0:len(s):1]
# s[::-1] : 끝에서 처음까지 1씩(거꾸로) == s[-1:-(len(s)+1):-1]


# 결합
'hello, ' + 'python!' # 'hello, python!'
# 반복
'hi!' * 3 # hi!hi!hi!
# 포함
'a' in 'apple' # True
'app' in 'apple' # True
'b' in 'apple' # False



import random
numbers = range(1, 46)
result = random.sample(numbers, 6)
print(result)