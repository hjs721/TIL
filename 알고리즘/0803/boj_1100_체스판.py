# matrix = []

# for _ in range(8):
#     line = list(input())
#     matrix.append(line)

matrix = [list(input()) for _ in range(8)]
result = 0
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0 and matrix[i][j] == 'F':
            result += 1
print(result)