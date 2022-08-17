import sys

sys.stdin = open("_모음이보이지않는사람.txt")

t = int(input())
out = ['a','e','i','o','u']

for test_case in range(1, t + 1):
    word = list(input())
    result = []
    print(f'#{test_case}', end = ' ')
    for i in word:
        if i not in out:
            result.append(i)
    print(*result, sep = '')



# remove랑 pop이 제대로 작동하지 않습니다. 제가 뭘 잘못 사용하고 있나요?ㅠㅠ
t = int(input())
out = ['a','e','i','o','u']
for test_case in range(1, t + 1):
    word = list(input())
    for i in word:
        if i in out:
            word.remove(i)
    print(*word, sep = '')
# 이 코드를 돌리면, 제 생각에는 반복문 돌면서 다 제거되어야 하는데 
# c n g r t l t o n
# s y n t h t c
# f l i d
# 출력값이 이렇게 지저분하게 나옵니다...

'''
A. remove()는 해당 리스트에 있는 모든 값을 삭제해 주는 것이 아니라 한 개의 값만 삭제해 준답니다!
즉 a = [1, 1, 0]이라는 리스트가 존재할 때 a.remove(1)을 진행하시면 a = [1, 0]이 되는 거죠
해당하는 모든 문자를 삭제해 주시기 위해서는 문자의 개수만큼 remove를 진행해야 해요!
'''


for test_case in range(1, t + 1):
    word = list(input())
    for i in range(len(word)):
        if word[i] in out:
            word.pop(i)
    print(*word, sep = '')
# 이 코드는 인덱스 에러가 납니다.

'''
A. pop()을 사용하시면 리스트에서 해당 값을 없애버리기 때문에 list의 길이는 점점 줄어들게 되겠죠
만약 원래 길이가 4인 리스트에 pop을 2번 진행하셨다면 리스트의 길이는 2가 됩니다.
그렇기 때문에 처음에 설정한 for i in range(4):에서 i 가 3이 되면 리스트의 길이는 이미 2가 되었기 때문에 list[3]이 존재하지 않아 인덱스 에러가 나게 됩니다!
'''