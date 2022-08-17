n, m = map(int, input().split())
nums = list(map(int, input().split()))

max_total = 0 # 현재 가장 큰 합
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            total = nums[i] + nums[j] + nums[k]
            if max_total < total <= m:
                max_total = total
            if total == m:
                break
print(max_total)