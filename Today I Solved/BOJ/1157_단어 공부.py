word = input().upper()
list_ = []
result = []
for i in word:
    list_.append(word.count(i))
for j in range(len(list_)):
    if list_[j] >= list_[j-1]:
        result.append(word[j])
result = set(result)
if len(result) == 1:
    print(*result)
if len(result) > 1:
    print('?')
# 이거 시간초과 뜸
# 반복문 하나로 풀어보기

word = input().upper()
s_word = list(set(word))
result = []
for i in s_word:
    cnt = word.count(i)
    result.append(cnt)
if result.count(max(result)) >= 2:
    print('?')
else:
    print(s_word[(result.index(max(result)))])
# 풀렸다!
# upper, set, count, max, index, append