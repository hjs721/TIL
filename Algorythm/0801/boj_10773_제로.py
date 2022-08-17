# inputs1 = [3, 0, 4, 0]
# inputs2 = [1, 3, 5, 4, 0, 0, 7, 0, 0, 6]

# 인풋이 0이면 가장 최신값 삭제 : stack에 pop
# 인풋이 0이 아니면 계속 입력 : stack에 append(push)
# 조건문 둘중에 뭘 골라야 좀더 편할까

K = int(input())
input_list = []
for _ in range(K):
    input_list.append(int(input()))
# 인풋 내용 핸들링 (맨 위처럼 리스트로 만듦)
stack = []
for elem in input_list:
    if elem != 0:
        stack.append(elem)
    else:
        stack.pop()
print(sum(stack))


# 줄이고 줄이면 이렇게 됨
stack = []
for _ in range(int(input())):
    number = int(input())

    if number == 0:
        stack.pop()
    else:
        stack.append(number)
        
print(sum(stack))