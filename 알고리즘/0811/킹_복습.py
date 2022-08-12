import sys
sys.stdin = open('킹.txt')

# 8방향 델타값
directions = {
    'R': (0, 1),
    'L': (0, -1),
    'B': (1, 0),
    'T': (-1, 0),
    'RT': (-1, 1),
    'LT': (-1, -1),
    'RB': (1, 1),
    'LB': (1, -1)
}
# 방향이 알파벳으로 입력되므로, 딕셔너리를 사용한다

k, s, n = input().split()

kx, ky = 8 - int(k[1]), ord(k[0]) - 65
sx, sy = 8 - int(s[1]), ord(s[0]) - 65

for _ in range(int(n)):
    move = input()
    mx, my = directions[move]
    # 범위 설정
    if not (0 <= kx + mx < 8 and 0 <= ky + my < 8):
        continue
    kx += mx
    ky += my

    # 킹의 위치와 돌의 위치가 겹쳤을 때
    if (kx, ky) == (sx, sy):
        if not (0 <= kx + mx < 8 and 0 <= ky + my < 8):
            kx -= mx
            ky -= my
            continue
        sx += mx
        sy += my

print(chr(ky + 65) + str(8 - kx))
print(chr(sy + 65) + str(8 - sx))