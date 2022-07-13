# word가 주어질 때 해당 단어에서 'a'를 모두 제거하여 출력하시오
# apple

word = input()
result = ''
# 반복
for i in word:
    # 만약 a 일 때
    if i != 'a':
        # 반복문에서 아무것도 안하고 넘어가는 것은? # continue
       result = result + i
print(result) # apple 입력하면 pple 나옴

word = 'apple'
result = ''
for i in word:
    if i != 'a':
        result = result + i
print(result)