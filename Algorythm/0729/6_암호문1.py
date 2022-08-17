import sys

sys.stdin = open("_암호문1.txt")


N = int(input())
# 11
org_list = list(map(int, input().split()))
# 449047 855428 425117 532416 358612 929816 313459 311433 472478 589139 568205
a = int(input()) # 명령어 총 갯수
# 7
명령어 = list(input()) # I, x, y, s 형태로 a개 
# I 1 5 400905 139831 966064 336948 119288
# I 8 6 436704 702451 762737 557561 810021 771706
# I 3 8 389953 706628 552108 238749 661021 498160 493414 377808
# I 13 4 237017 301569 243869 252994
# I 3 4 408347 618608 822798 370982
# I 8 2 424216 356268
# I 4 10 512816 992679 693002 835918 768525 949227 628969 521945 839380 479976

# 출력:
# 449047 400905 139831 408347 512816 992679 693002 835918 768525 949227


# 손도 못대겠어요.....


# insert(삽입위치, 값) 메서드

# 명령어 = 명령어리스트[0]
# if 명령어 == "I":
#     x = 명령어리스트[0 + 1]
#     y = 명령어리스트[0 + 2]
#     숫자_리스트 = 명령어리스트[0 + 3 : 0 + 3 + y]

# for 숫자 in 숫자_리스트[::-1]:
#     암호문.insert(삽입 인덱스, 숫자)



# 원본암호문 = [449047, 855428, 425117, 532416, 358612, 929816, 313459, 311433, 472478, 589139, 568205]
T = 10
for t in range(1, T + 1):
    origin_len = int(input())
    origin_list = list(map(int, input().split()))

    command_len = int(input())
    command_list = input().split()

    # i의 초기화
    i = 0
    # while문(반복문)
    while i < len(command_list):
        command = command_list[i]
        if command == "I":
            # x, y, 숫자리스트 s 구해야
            x = int(command_list[i + 1])
            y = int(command_list[i + 2])
            number_list = command_list[i + 3 : i + 3 + y]
            # insert 메서드를 써서 x의 위치에 숫자들을 삽입한다.
            # 역순으로!
            for number in number_list[::-1]:
                origin_list.insert(x, int(number))
        # 0 -> 1
        i = i + 1
    print(f'#{t}', *origin_list[:10])
    # *리스트이름 : 언패킹...... 리스트 대괄호 벗겨줌