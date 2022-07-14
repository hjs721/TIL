# 리스트는 mutable
a = [1, 2, 3]
a[0] = 100
print(a) # [100, 2, 3]
# 리스트는 바꿀 수 있다~!

# 문자열은 imutable
a = 'hi'
a[0] = 'c'
print(a) # error
# 문자열의 첫번째 인덱스에 해당하는 값을 바꿀수는 없다~!!