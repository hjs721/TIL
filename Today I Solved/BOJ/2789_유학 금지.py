word = input()
minus_ = ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']
result = []
for i in word:
    if i not in minus_:
        result.append(i)
print(*result, sep='')