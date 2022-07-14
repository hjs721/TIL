# 문자열 word가 주어질 때, 해당 문자열에서 모음의 갯수를 출력하시오.
# 모음 : a, e, i, o, u 
# count() 사용 금지

word = input()
result = 0
for char in word:
    if char == 'a':
        result += 1
    elif char == 'e':
        result += 1
    elif char == 'i':
        result += 1
    elif char == 'o':
        result += 1
    elif char == 'u':
        result += 1
print(result)

# 강사님 풀이
for char in word:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        result += 1
print(result)

result = 0
for char in word:
    # ['a', 'e', 'i', 'o', 'u']
    if char in 'aeiou':
        result += 1
print(result)