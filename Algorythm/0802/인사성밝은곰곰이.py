# if 닉네임 not in set:
#     set.add(닉네임)
#     곰 += 1
# if 닉네임 == 'ENTER':
#     set.clear()

N = int(input())
gom = 0
log_list = list(input())
set_ = set()
for log in log_list:
    if log == 'ENTER':
        set_.clear()
    else:
        if log not in set_:
            set_.add(log)
            gom += 1
print(gom)