sum = 5
print(sum([1,2,3])) # 오류남
# TypeError: 'int' object is not callable
# built-in scope 에 sum 함수가 있었음
# Global scope에 sum 이름의 변수를 만들었음
# 찾을때는 L-E-G-B 순서로 찾음
# sum이 지금은 5가 되어버림... 함수 기능을 못하게 돼서 print 안에 써도 기능x