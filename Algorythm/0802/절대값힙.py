from heapq import
N = 18
heap = []
X = [1, -1, 0, 0, 0, 1, 1, -1, -1, 2, -2, 0, 0]

heappush(heap ([abs(x), x]))
root = heappop(heap)
print(root[1])