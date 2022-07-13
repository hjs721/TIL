for char in 'apple':
    if char == 'b':
        print('b!')
    else:
        print(char) # 이거 없으면 철자는 안나옴
else:
    print('b가 없습니다.')


for number in [10, 20, 30]:
    if number == 10:
        print('10!')
else:
    print('10이 아닙니다.')