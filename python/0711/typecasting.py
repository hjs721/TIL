# 문자열 안에 변수 넣기
score = 100

# 내 점수는 100이야.
print('내 점수는 ' + str(score) + '이야.')

# 문자열은 암시적 타입 변환 안됨
'3' + 4 # 오류

# 명시적 타입 변환 필요
int('3') + 4 #7

# 정수 형식이 아닌 경우 변환할 수 없음
int('3.5') + 5 # 오류
float('3.5') + 5 # 8.5