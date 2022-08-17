T = int(input()) # 5
for test_case in range(1, T + 1):
    A, B = map(int, input().split())
    print(f'Case #{test_case}: {A + B}')