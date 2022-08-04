# 이름을 키로 사용해서 저장할 딕셔너리 변수
# dict_ = dict()
# dict_['ohhenrie'] = '듣도 못한 사람'
# dict_['charlie'] = '듣도 못한 사람'
# dict_['baesangwook'] = '듣도 못한 사람'

# if 'obama' in dict_:
#     print('obama 듣도 보도 못한 사람')
# if 'baesangwook' in dict_:
#     print('baesangwook 듣도 보도 못한 사람')
# if 'ohhenrie' in dict_:
#     print('ohhenrie 듣도 보도 못한 사람')
# if 'clinton' in dict_:
#     print('clinton 듣도 보도 못한 사람')

N, M = map(int, input().split())
dict_ = dict()
for i in range(N): # N의 크기만큼 듣도 못한 사람 입력
    p = input()
    dict_[p] = '듣도 못한 사람'

list_ = []
for i in range(M): # M의 크기만큼 보도 못한 사람 입력
    p = input()
    if p in dict_: # 입력받은 사람이 딕셔너리의 키 중에 있느냐?
        list_.append(p)
list_.sort()
print(len(list_))
for p in list_:
    print(p)