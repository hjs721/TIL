word = 'banana'

def transform_uppercase(word):
    result = ''
    for char in word:
        number = ord(char)
        number = number-32
        result += chr(number)
    return result
for word in word:
    print(transform_uppercase(word))

word = 'banana'
word.upper()

my_list = [1, 2, 3]
# 리스트.sort()
#리스트의 데이트를 직접 정렬
my_list.sort()

my_lsit = [1, 2, 3]
# 리스트는 sorted 함수의 인자로 전달될 뿐
my_list = sorted(my_list)
# 단순 sorted()만으로는 아무 의미도 가지지 못함. 반드시 무언가로 정의해줘야