n = 0
result = 0
user_input = int(input())

while n <= user_input:
    result += n
    n += 1
print(result)

# while
n = 10
i = 0
result = 0
while i <= n:
    result += i
    i += 1
print(result)

# for
n = 10
i = 0
result = 0
for i in range(n+1): # rnage에는 +1해야됨! chars[0], chars[1] 출력하려면 range(2)를 씀
    result += i
    i += 1
print(result)