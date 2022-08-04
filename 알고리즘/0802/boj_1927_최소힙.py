# minheap
import heapq

heap = [] # heapify 안해도 됨

for _ in range(int(input())):
    n = int(input())
    # 자연수면 -> 추가(heappush)
    if n != 0:
        heapq.heappush(heap, n)
    # 0이면 -> 작은값 제거(heappop)
    else:
        if len(heap) == 0: # 여기서 == 0 생략 가능
            print(0)
        else:
            print(heapq.heappop(heap))