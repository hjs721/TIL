numbers = [0, 20, 100]
max = numbers[0]
for i in numbers:
    if max <= i:
        max = i
print(max)

numbers = [0, 20, 100, 50, -60, 50, 100] # 100
max = numbers[0]
for i in numbers:
    if max <= i:
        max = i
print(max)

numbers = [0, 1, 0] # 1
max = numbers[0]
for i in numbers:
    if max <= i:
        max = i
print(max)

numbers = [-10, -100, -30] # -10 
max = numbers[0]
for i in numbers:
    if max <= i:
        max = i
print(max)

# for문을 통해서 numbers 수를 차례차례 거쳐가고 그 과정에서 max보다 큰 수가 나타나면 max값을 해당 값을 바꿔줍니다!
# 그러면 자동으로 max에는 가장 큰 값이 들어갈테니까 출력해주시면 돼요 ㅎㅎ