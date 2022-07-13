# 주어진 문자열 word가 주어질 때 해당 단어를 역순으로 뒤집은 결과를 출력하시오

word = input()
result = ''
for i in word:
    result = i + result # < 앞에 한글자씩 더하는거.. a + '', pa + '', ppa + '' 형식
print(result)

print(word[::-1])