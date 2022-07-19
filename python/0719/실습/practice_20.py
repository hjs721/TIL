# 정수 number가 주어질 때, 각 자릿수의 합을 구해서 출력하세요. 
# input : 123
# output : 6

number = str(input())
sum = 0
for i in range(len(number)):
    sum += int(number[i])
print(sum)


# 정답
number = 123
# number가 0일때 Stop!
# int는 0일 때 False
result = 0
while number:
    # 10으로 나눔
    # 몫은 다음 numebr가 될거고, 나머지는 더해나가면 된다!
    result += number % 10
    number //= 10
print(result)

# 내장함수 divmod(x, y)는 x를 y로 나누고, 결과를 tuple로 반환함
# (몫, 나머지)
number = 123
result = 0
while number:
    numebr, remainder = divmod(number, 10)
    result += remainder