# > 소문자로 구성된 문자열 word가 주어질 때, 모두 대문자로 바꾸어 표현하시오.
# `**.upper()`, `.swapcase()` 사용 금지**

# ord('a') 
# 97
# chr(97)
# 'a'

word = input()
for i in word:
    if ord(i) >= 97:
        iupper = chr(ord(i) - 32)
        print(iupper, end='')

# 강사님 정답