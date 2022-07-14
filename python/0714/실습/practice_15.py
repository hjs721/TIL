# 문자열 word가 주어질 때, 해당 문자열에서 a 가 처음으로 등장하는 위치(index)를 출력해주세요.
# a 가 없는 경우에는 -1을 출력해주세요.
# find() index() 메서드 사용 금지

print(input().find('a'))

word = input()
for i in range(len(word)):
    if word[i] == 'a':
        print(i)
        break
# 답안에서는 else:print(-1) 하라는데 안해도 -1 출력됨 왜지?

# 만약 a가 있었나 없었나가 알고 싶다면? (bloolean불리언)
is_a = False
for idx in range(len(word)):
    if word[idx] == 'a':
        print(idx)
        is_a = True
        break

# 문자열 word가 주어질 때, 해당 문자열에서 a 의 모든 위치(index)를 출력해주세요.
# find() index() 메서드 사용 금지

word = 'HappyHacking'
for i in range(len(word)):
    if word[i] == 'a':
        print(i, end=' ')

# 강사님 풀이
word = 'banana'
result = []
for idx in range(len(word)):
    if word[idx] == 'a':
        print(idx, end=' ')