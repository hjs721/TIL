'''
N 이하, 4와 7로만 이루어진 숫자 중 가장 큰 수 출력
자릿수를 탐색, 4와 7로만 이루어져있는지 확인
'''

# 숫자 N 입력
N = int(input())

# 초기 가장 큰 값 N은 4
max_ = 4

for number in range(N + 1):
    # 숫자를 문자열로 변환
    string_number = str(number)

    # 각 숫자의 자릿수 값 확인
    for char_number in string_number:
        # 각 자릿수가 4 또는 7로만 이루어져있는지 확인
        # 각 자릿수가 4 또는 7로만 이루어져있지 않으면 반복 종료. break
        if not(char_number == '4' or char_number == '7'):
            break
        # for~ else: for이 정상적으로 다 완료되면 else 실행
        # break를 만나지 않으면 else가 실행됨!
        else:
            # 최댓값 갱신
            max_ = int(string_number)

print(max_)