import heapq

# heapq.heapify() : 힙큐화(느슨한 정렬)
# heapq.heappop(heap) : 최솟값 팝
# heapq.heappush(heap, item) : 값 추가

numbers = [5, 3, 2, 4, 1]

heapq.heapify(numbers)
# 리스트같은 시퀀스형 자료형 넣어주면 heap형으로 바뀜
# 원본 바꿈(훼손)(디스트럭티브 메소드)

print(numbers) # [1, 3, 2, 4, 5]
# 느슨한 정렬

heapq.heappop(numbers)
# 1 팝핑

print(numbers) # [2, 3, 5, 4]
# 다시 제일 작은 값을 맨 앞에

heapq.heappop(numbers)

print(numbers) # [3, 4, 5]

heapq.heappush(numbers, 10)
heapq.heappush(numbers, 0)

print(numbers) # [0, 3, 5, 10, 4]