a = [1, 2, 3]
b = a
b[0] = 'hi'

print(a) # ['hi', 2, 3]
print(b) # ['hi', 2, 3]
# 변수 = 메모리 주소값
# a도 b도 같은 주소를 가지기 때문에 b를 바꾼 순간 a도 바뀜

# 얕은 복사
# list 형변환 결과 : 사실은 list고 사실은 값도 같지만 다른 메모리 주소 결과를 받아냄
c = [3, 4, 5]
d = list(c)
d[0] = 'hi'
print(c) # [3, 4, 5]
print(d) # ['hi', 4, 5]

# 슬라이싱
e = [4, 5, 6]
f = e[::]
f[0] = 'hi'
print(e) # [4, 5, 6]
print(f) # ['hi', 5, 6]


# 깊은 복사
a = [[1, 2], 2, 3]
b = list(a)
b[0][0] = 'hi'
print(a) # [['hi', 2], 2, 3]
print(b) # [['hi', 2], 2, 3]

import copy
a = [[1, 2], 2, 3]
b = copy.deepcopy(a)
b[0][0] = 'hi'
print(a) # [[1, 2], 2, 3]
print(b) # [['hi', 2], 2, 3]