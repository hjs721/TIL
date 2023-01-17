a = [0, 1]
# 접근
print(a[0])
# 변경
# 인덱스가 0에 해당하는 값을 -1로 바꾼다
a[0] = -1
print(a)

# 생성
my_list = []
another_list = list()
type(my_list)
# <class 'list'>
type(another_list)
# <class 'list'>

even_numbers = [2, 4, 6, 8]
# 추가하고자 하는 v값v을 전달
even_numbers.append(10)
print(even_numbers)  # [2, 4, 6, 8, 10]
# 삭제하고자 하는 v인덱스v를 전달
even_numbers.pop(0)
print(even_numbers)  # [4, 6, 8, 10]

# 예제
boxes = ["apple", "banana"]
print(len(boxes))  # 2
print(boxes[1])  # banana
print(boxes[1][0])  # b
