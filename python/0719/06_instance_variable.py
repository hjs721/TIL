class Person:
    pass


# Person 클래스의 인스턴스 iu
iu = Person()
# iu의 인스턴스 변수 할당
iu.nmae = '아이유'
iu.age = 30
iu.gender = 'F'
# 인스턴스 변수 접근 #출력
print(iu.nmae)

class Info:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
iu = Info('아이유', 30, 'F')
print(iu.gender)
# 알겠다!