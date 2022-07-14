# .append(x)
# 리스트 마지막!!!에 항목 x 추가

a = ['apple']
a.extend(['banana', 'mango'])
print(a)
a.extend('banana')
print(a) # ['apple', 'banana', 'mango', 'b', 'a', 'n', 'a', 'n', 'a']
# .extend에는 무조건 ''리스트''를 넣어야 함!!!!

# .insert(i, x)

# .remove(x)

# .pop(i)
# i 위치에 있는 값 삭제. i 비워두면 마지막 항목 삭제

# .clear()
# 모든 항목 삭제, 빈 리스트 출력

# .index(x)

# .count(x)
# 원하는 값(x)의 개수를 반환

# .sort()

# .revers()
# 순서를 반대로 뒤집음(정렬은 안해주고 그냥 뒤집기만)
numbers = [3, 2, 5, 1]
result = numbers.reverse()
print(numbers, result)
# [1, 5, 2, 3] None
# 원본이 변경되므로 numbers만 출력해도 됨