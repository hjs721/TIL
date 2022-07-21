# 리스트 컴프리헨션
# 홀짝으로 더하고 빼는 문제
# 0 -1 +2 -3

numbers = [0, 1, 2, 3]

even_list = [i for i in range(10) if i % 2 == 0]
print(even_list)
# 이런 식으로 간단한 리스트를 만들때 리스트 컴프리헨션을 사용할 수 있음
print(sum(even_list))


# 딕셔너리 컴프리헨션
