#f-string(string formatting)
#문자열에서 특정 부분만 바꾸고 나머지 부분은 일정할 때 사용
#변해야 할 값이 있는 부분은 {} 사용

#2단부터 9단까지 반복하여 구구단을 출력하세요.
#* 문자열 출력시 f-string(f'n: {n}, result: {result}')을 활용하면 편하게 작성할 수 있습니다.

# output
#2단
#2 X 1 = 2 
#2 X 2 = 4
#...
#3단
#3 X 1 = 3 
#3 X 2 = 6
#...생략...

for a in range(2, 10):
    print(f'{a}단')
    for b in range(1, 10):
        print(f'{a} X {b} = {a * b}')