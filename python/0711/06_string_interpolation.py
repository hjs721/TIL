# 문자열 안에 변수 넣기
score = 100

# 내 점수는 100이야.
# print('내 점수는 ' + score + '이야.')
# 만약 name 이었다면 오류가 발생하지 않았을 것(str이니까)
print(f"내 점수는 {score}이야.")

pi = 3.141592
r = 2
print(f"원주율은 {pi:.3}고, 원 넓이는 {pi*r*r}야.")

# 문자열을 변수를 활용해서 만드는 법 : %s(문자열), %d(정수), %f(실수) but 불편하면 앞에 f만 붙이면 됨

name = "Kim"
score = 4.5
print("Hello, %s" % name)
print("Your score is %d" % score)
print("Your score is %f" % score)

# 파이썬은 앞에 f만 붙이면 되는데 C나 자바에서는 저렇게 많이 씀

# 문자열 특징
# Immutable : 변경 불가능 (인덱싱으로 요소 변경 불가능)
# Iterable : 반복 가능
a = "123"
for char in a:
    print(char)
