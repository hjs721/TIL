import sys

sys.stdin = open("_문자열의거울상.txt")


change_dict = {
    'b': 'd',
    'd': 'b',
    'p': 'q',
    'q': 'p'
}
T = int(input())
for test_case in range(1, T + 1):
    word = input()
    word = word[::-1]
    list_ = []
    for i in word:
        list_.append(change_dict[i])
    print(*list_, sep = '') # 리스트를 어떻게 문자열로 변환하는지 모르겠다...... :: 이거 찾음!!!! 리스트앞에 *