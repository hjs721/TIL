# 100을 사용자가 입력한 숫자로 나눠서 결과를 출력
number = input()

try:
    print(100/int(number))
# except exception:
    # print('오류')   # 맨 위에서 상위개념을 넣어버리면 0이든 글자든 전부 오류라고만 뜸
except ZeroDivisionError:
    print(err) # 에러 종류 보여줌 # division by zero
    print('0으로 나눌 수는 없습니다.')
except ValueError:
    print('숫자 형식을 입력해주세요.')
except Exception:
    print('오류')  # 따라서 맨 밑에 넣어줘야 함

try:
    print(100/int(number))
except ZeroDivisionError, ValueError:
    print('제대로 입력해줘')  # 이것도 됨