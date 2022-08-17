import sys
sys.stdin = open('애너그램.txt')

t = int(input())
for _ in range(t):
    a, b = input().split()
    A = sorted(list(a))
    B = sorted(list(b))
    if A == B:
        print(f'{a} & {b} are anagrams.')
    else:
        print(f'{a} & {b} are NOT anagrams.')