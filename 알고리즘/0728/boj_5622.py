word = input() # 들어갈 단어 # WA
num = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
result = 0 # 걸리는 시간
for i in range(len(word)): # 2
    for j in num: # WXYZ, ABC
        if word[i] in j: # W, A
            result += num.index(j) + 3 # 인덱스는 0~7 # W 할당값 10, A 할당값 3 # (7 + 3) + (0 + 3)
print(result)


# 딕셔너리
dict_ = {
    'A': 2, 'B': 2, 'C': 2,
    'D': 3, 'E': 3, 'F': 3,
    'G': 4, 'H': 4, 'I': 4,
    'J': 5, 'K': 5, 'L': 5,
    'M': 6, 'N': 6, 'O': 6,
    'P': 7, 'Q': 7, 'R': 7, 'S': 7,
    'T': 8, 'U': 8, 'V': 8,
    'W': 9, 'X': 9, 'Y': 9, 'Z': 9
}

time_ = 0
string = input()
for key in string:
    number = dict_[key]
    time_ += number + 1
print(time_)