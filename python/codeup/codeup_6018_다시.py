a = '1 2 3' # 을 쪼개서 하나씩 쓸 수 있는 방법
print(a.split()) # 리스트! ['1', '2', '3']

numbers = a.split()
result = int(numbers[0]) + int(numbers[1]) + int(numbers[2])
print(result) # 헐 이해된다

a = '10:20' # 이경우 인덱스가 단일이고 수치 길이가 있으니까 스플릿하면 리스트가 나옴
numbers = a.split(':') # :을 기준으로 스플릿
print(numbers) # ['10', '20']
print(numbers[0], numbers[1], sep=':') # 출력할 때 sep을 작성하면 값 사이에 해당 문자를 넣어서 출력

# 정답
a, b = input().split() # 이 경우 인덱스 자체가 두개니까 스플릿하면 걍 a랑 b가 남음 # 별도로 쓸 수 있음
print(a, b, sep=':')