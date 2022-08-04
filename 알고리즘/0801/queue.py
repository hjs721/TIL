from collections import deque

numbers = [1, 2, 3, 4, 5]

queue = deque(numbers)

queue.append(6) # 넣을 때

queue.popleft() # 뺄 때 # 인자가 안들어감

print(queue) # deque([2, 3, 4, 5, 6])

for num in queue:
    print(num, end = ' ') # 2 3 4 5 6 

print(list(queue)) # [2, 3, 4, 5, 6]