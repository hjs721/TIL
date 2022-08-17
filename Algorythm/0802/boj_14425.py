S = []
words = []

# 풀이 1
cnt = 0
word_set = set(S)
for word in words:
    if word in word_set: # S, set(S) 속도 비교
        cnt += 1
print(cnt)

# 풀이 2
print(len(set(words) & set(S))) # 교집합