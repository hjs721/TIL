# 인풋값 리스트에 집어넣기
list_ = []
for _ in range(9):
    list_.append(int(input()))

# 두개 뽑아서
for i in range(8):
    for j in range(i + 1, 9):
        # 전체합에서 두개 뺐을때 값이 0이면
        if sum(list_) - (list_[i] + list_[j]) == 100:
            a = list_[i]
            b = list_[j]
list_.remove(a) # 리스트에서 제거
list_.remove(b)
result = sorted(list_) # 정렬
print(*result, sep = '\n') # 개행 나눠서 출력