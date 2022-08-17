r, c = map(int, input().split())
matrix = [list(input().split()) for _ in range(r)]

dx = [0, 1, 0, 1]
dy = [0, 0, 1, 1] # 2행 2열 델타탐색(원본, 우, 하, 우하)

result = [0] * 5

def locate(x, y):
    # 부숴야하는 차의 갯수
    cnt = 0

    for dx, dy in (0, 0), (1, 0), (0, 1), (1, 1):
        if matrix[x + dx][y + dy] == '#':
            return -1
        elif matrix[x + dx][y + dy] == 'X':
            cnt += 1
    return cnt


# 코드리뷰 # 강의 다시 들어보기...
# 델타탐색
# dx = [1, 0, 1]
# dy = [0, 1, 1]

# for d in range(3):
#     ny = y + dy[d]
#     nx = x + dx[d]

# # 이중 리스트 탐색
# for y in range(r):
#     for x in range(c):
#         # 기준 좌표의 값이 빌딩이면 continue
#         if list_[y][x] == '#':
#             continue
#         # 부순 차의 개수를 기준 좌표로 옮길 때마다 초기화(0)
#         break_count = 0
#         # 기준 좌표의 값이 차라면 부순 차의 개수 + 1
#         if list_[y][x] == 'X':
#             break_count += 1

from pprint import pprint

# 우, 우하, 하
# x + 1, (y + 1, X + 1), y + 1
da = [0, 1, 1]
db = [1, 1, 0]

building = '#'
car = 'X'
void = '.'

# 숫자가 공백으로 나뉘어져있는 입력
r, c = list(map(int, input().split()))
list_= []

# R줄만큼의 리스트를 입력
for _ in range(r):
    # 숫자 아님. 문자
    # 띄어쓰기 없음
    temp_list = list(input())
    list_.append(temp_list)

# 부순 횟수를 저장할 리스트
break_count_list = [0] * 5

# 이중 반복문
for a in range(r):
    for b in range(c):
        # 차를 부순 횟수는 탐색할때마다 초기화(0)
        break_count = 0
        # 조건1. 기준 좌표가 빌딩(#)이면 안된다.
        if list_[a][b] == building:
            # 이 다음 반복문의 코드들을 무시하고, 다음 값을 선택
            continue
            # 성립이 안되는 조건들은 continue로 지나가버림
            # 조건이 성립될때만 정상적인 코드 실행
        # 조건2. 기준좌표가 차라면 부순 횟수가 +1
        if list_[a][b] == car:
            break_count += 1

        # 여기서부터 델타탐색 로직
        for d in range(3):
            next_a = a + da[d]
            next_b = b + db[d]
            # 조건 1. 범위를 벗어나면 안된다.
            if not (-1 < next_a < r and -1 < next_b < c):
                break
            # 조건 2.  탐색 좌표에 빌딩이 있으며 ㄴ안된다.
            if list_[next_a][next_b] == building:
                break
            # 조건3. 탐색 좌표에 차가 있으면 부순 횟수를 +1
            if list_[next_a][next_b] == car:
                break_count += 1
        # break를 만나지 않고 for 문이 끝났다면
        # 해빈이가 정상적으로 주차했다는 뜻
        else:
            break_count_list[break_count] += 1

for count in break_count_list:
    print(count)