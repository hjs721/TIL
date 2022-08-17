stack_list = [[12, 4, 1], [6, 2], [9, 7, 3], [11, 10, 8, 5]]
answer = "Yes"
# 비교값을 pop 통해 스택에서 꺼내온다
# 5
for stack in stack_list:
    comparison = stack.pop()
    # 스택이 비어있지 않을 때는 계속/스택 비면 종료
    while len(stack) != 0: # while 문으로 스택 순회할때 가장 많이 쓰는 방법
        # top comparison 비교
        if stack[-1] > comparison: # stack[-1] = top
            # pop 사용해서 comparison 값 갱신
            comparison = stack.pop()
        else:
            answer = "No"
            break
    if answer == "No": # 이부분은 안넣어도 됨
        break
print(answer)