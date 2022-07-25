# 세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.

# 예를 들어 A = 150, B = 266, C = 427 이라면 A × B × C = 150 × 266 × 427 = 17037300 이 되고, 계산한 결과 17037300 에는 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다.

# 입력
# 첫째 줄에 A, 둘째 줄에 B, 셋째 줄에 C가 주어진다. A, B, C는 모두 100보다 크거나 같고, 1,000보다 작은 자연수이다.
# 150
# 266
# 427

# 출력
# 첫째 줄에는 A × B × C의 결과에 0 이 몇 번 쓰였는지 출력한다. 마찬가지로 둘째 줄부터 열 번째 줄까지 A × B × C의 결과에 1부터 9까지의 숫자가 각각 몇 번 쓰였는지 차례로 한 줄에 하나씩 출력한다.
# 3
# 1
# 0
# 2
# 0
# 0
# 0
# 2
# 0
# 0


A = int(input()) # 150
B = int(input()) # 266
C = int(input()) # 427
result = str(A * B * C) # 숫자 자리마다 인덱스 처리해서 순회해야 함 => str이나 list 변환
for i in range(10): # 순회는 for
    cnt = 0 # 기본값 설정
    for a in range(len(result)): # 곱셈한 값의 각 자리 숫자가
        if result[a] == str(i): # 0~9 중 하나와 같다면
            cnt += 1 # 그 자리에 맞춰서 cnt 1씩 증가
    print(cnt)


A = int(input())
B = int(input())
C = int(input())
result = str(A * B * C)
for i in range(10):
    print(result.count(str(i))) # str형은 count 메서드 사용 가능