# 어떤 수 X가 주어졌을 때, X의 모든 자리수가 역순이 된 수를 얻을 수 있다. Rev(X)를 X의 모든 자리수를 역순으로 만드는 함수라고 하자. 예를 들어, X=123일 때, Rev(X) = 321이다. 그리고, X=100일 때, Rev(X) = 1이다.
# 두 양의 정수 X와 Y가 주어졌을 때, Rev(Rev(X) + Rev(Y))를 구하는 프로그램을 작성하시오

# 입력
# 첫째 줄에 수 X와 Y가 주어진다. X와 Y는 1,000보다 작거나 같은 자연수이다.
# 123 100

# 출력
# 첫째 줄에 문제의 정답을 출력한다.
# 223

X, Y = input().split()
def Rev(X):
    return int(X[::1])
def Rev(Y):
    return int(Y[::-1])
result = str(Rev(X) + Rev(Y))
def Rev(result):
    return int(result[::-1])
print(Rev(result))
# 같은 연산이니 함수 하나만 설정해도 될듯?
# print 안에서 이래저래 만들어보자

    
# 코드 줄이기
def Rev(X):
    a = int(X[::-1])
    return a
x, y = input().split()
print(Rev(str(Rev(x)+Rev(y))))