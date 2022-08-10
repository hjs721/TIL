'''
가장 많은 문자를 출력. 여러개라면 사전순으로 출력
'''

# 문자를 카운팅하는 로직
dict_ = {}
# 입력의 개수가 정해져있지 않기 때문에 while 사용
while True:
    '''
    예외 처리 try ~ except~
    try: 정상적으로 실행될 때(오류 x)
    except : 오류가 발생할 때 실행되는 코드 블럭
    '''
    # 정상적인 경우, 에러가 없는 경우
    try:
        input_ = input()
        inpupt_ = input_.replace(' ', '')

        # 문자 개수 카운팅
        for char in input_:
            # 문자가 딕셔너리의 key 중 하나가 아니라면 value로 1 할당
            # 딕셔너리의 key 중 하나라면 value += 1
            if char not in dict_:
                dict_[char] = 1
            else:
                dict_[char] += 1
    except:
        break

print(dict_.items()) # 튜플
# x는 dict_.items()에 의해 만들어진 각 튜플
# 튜플의 인덱스1(숫자) 먼저 고려, 문자 사전순정렬은 두번째
sorted_dict = sorted(dict_.items(), key = lambda x: (-x[1], x[0]))
max_ = sorted_dict[0][1]
for char, count in sorted_dict:
    if max_ == count:
        print(char)