set_a = {1, 2, 3, 1, 1}
set_b = {"hi", 1, 2}
# 중복제거해서 유일한 값만 전달
print(set_a)  # {1, 2, 3}
print(set_b)  # {1, 2, 'hi'}

numbers = {1, 2, 3}
numbers.add(5)
print(numbers)  # {1, 2, 3, 5}
numbers.add(1)
print(numbers)  # {1, 2, 3, 5}

numbers = {1, 2, 3}
numbers.remove(1)
print(numbers)  # {2, 3}
# numbers.remove(5)
# print(numbers)  # 오류

# 세트를 활용하면 다른 컨테이너에서 중복된 값을 쉽게 제거할 수 있음 :: 단!!! 이후 순서가 무시되므로 순서가 중요한 경우 사용할 수 없음

# 예제
locations = ["서울", "서울", "대전", "광주", "서울", "대전", "부산", "부산", "대구", "제주", "대구"]
print(set(locations))  # {'광주', '서울', '제주', '대전', '부산', '대구'}
