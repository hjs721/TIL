from collections import deque

n = int(input())
queue = deque(range(1, n + 1))

while len(queue) > 1:
    print(queue.popleft(), end = ' ') # 맨첫번째 숫자 뽑고
    queue.append(queue.popleft()) # 그 다음 숫자 뽑아서 맨 뒤에 추가 -> 이걸 while로 무한반복

print(queue[0]) # 마지막 인자까지 출력