numbers = [0, 20, 100, 40]
max = numbers[0]
sec_max = numbers[0]

# 1. 전체 숫자를 반복
for i in numbers:
    # 만약에 i가 최대보다 크다면
    if max < i:
        # 최대값이었던 것이 두번째로 큰 수가 됨
        sec_max = max
        max = i
print(sec_max)
# 머가 틀린지 모르겠네 하........