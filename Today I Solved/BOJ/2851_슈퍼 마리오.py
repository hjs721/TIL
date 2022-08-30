# 리스트 컴프리헨션
score = [int(input()) for _ in range(10)]
result = 0
for i in score:
    result += i
    if result >= 100:
        if result - 100 > 100 - (result - i):
            result -= i
        break
print(result)