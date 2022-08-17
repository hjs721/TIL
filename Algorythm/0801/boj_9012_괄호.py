import sys
sys.stdin = open("괄호.txt")

T = int(input())
for test_case in range(T):
    n = input()
    stack_ = [] # 스택으로 풀어보자
    bool_ = True
    for i in n:
        if i == '(':
            stack_.append(i) # 여는 괄호일때 스택에 쌓아줌
        else: # 닿는 괄호일때 하나씩 빼주면 되는데
            if len(stack_) == 0: # 빼려면 값이 있어야 하니까 0일 때는 못 뺌
                print('NO') # No 출력하고
                bool_ = False
                break # 반복문 종료
            else: # 뺄 값 있으면
                stack_.pop() # 여는괄호 하나씩 날려주면 됨
    if bool_:
        if len(stack_) == 0: # 그렇게 해서 남은게 없으면
            print('YES') # Yes 출력
        else: # 스택에 남은게 있으면
            print('NO') # No 출력

# len(stack_) == 0 라인이 중복됨
# 불리언 변수를 추가해서 구분하자!
# 대소문자 구분 제발...........


# 강사님 풀이
bracket_list = list(input())
left = '('
right = ')'
left_stack = [] # 스택 두개 만들어서 풀기
right_stack = []
for bracket in bracket_list:
    if bracket == left:
        left_stack.append(bracket)
    if bracket == right:
        if len(left_stack) != 0:
            left_stack.pop()
        else:
            right_stack.append(bracket)
if len(left_stack) == 0 and len(right_stack) == 0:
    print('YES')
else:
    print('NO')