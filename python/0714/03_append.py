a = [1, 2, 3]
a = a.append(4)
# a.append(4)의 반환값을 a에 저장해버림
# 리스트.append()의 메서드는 반환값은 None!
print(a) # None

b = [1, 2, 3, 4]
b.append(5)
print(b) # [1, 2, 3, 4, 5]