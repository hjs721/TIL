result = []
for i in range(5):
    if 'FBI' in input():
        result.append(i + 1)
if len(result) == 0:
    print('HE GOT AWAY!')
else:
    print(*result)
