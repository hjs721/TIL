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

# A1 = (7, 0)
kx, ky = 8 - int(k[1]), ord(k[0]) - 65 # king x, y
sx, sy = 8 - int(s[1]), ord(s[0]) - 65 # stone x, y

road=[]
for i in range(int(n)):
    now=sys.stdin.readline().strip()
    road.append(dic[now])
for i in range(N):
    dx,dy=road[i]
    if king[0]+dx<0 or king[0]+dx>=8 or king[1]+dy<0 or king[1]+dy>=8:
        pass
    elif king[0]+dx==stone[0] and king[1]+dy==stone[1]:
        if stone[0]+dx<0 or stone[0]+dx>=8 or stone[1]+dy<0 or stone[1]+dy>=8:
            pass
        else:
            king=(king[0]+dx,king[1]+dy)
            stone=(stone[0]+dx,stone[1]+dy)
    else:
        king=(king[0]+dx,king[1]+dy)


print(chr(king[0]+65)+str(king[1]+1))
print(chr(stone[0]+65)+str(stone[1]+1))