# 주어진 숫자를 뒤집은 결과를 출력하시오. 
# * 문자열이 아닌 숫자로 활용해서 풀어주세요. str() 사용 금지
# 십진수 원리 사용하면 된다고 하는데 될까나

number = 12345
result = 0
# 1. str 쓰지 말라고했지만 그래도 일단
print(str(number)[::-1])
# 2. while로 몫과 나머지
while number:
    # 이전 결과에 10을 곱하고
    result *= 10
    # 나머지를 더해주고
    result += number % 10
    # number를 깎는다
    number //= 10
print(result)