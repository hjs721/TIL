# 1. num은 input으로 사용자에게 입력을 받으세요.
num = int(input())
# print(num)으로 되는지 확인
# 2. 조건문을 통해서 홀수/짝수 여부를 출력하세요

if num % 2 == 1:
    print('홀수')
else:
    print('짝수')
# 이러면 오류남 - 숫자로서의 num이어야! # print(num, type(num)) 실행해보면 str 나옴
# input은 문자열만 받기 때문에 int로 감싸줘야 함!!!!!!!!!!!
# 따라서 int로 형변환을 해야 함 # int로 감싸고 나서 print(num, type(num))하면 int 나옴