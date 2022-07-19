class Person:

    # 생성자! 인스턴스가 생성될 때 어떠한 작업! 기본적인 값세팅 등
    def __init__(self, name):
        # 그 인스턴스의 이름을 name으로 해주세요
        self.name = name

# Person 클래스의 인스턴스인 iu를 생성, jimin을 생성
iu = Person('이지은')
print(iu.name)
jimin = Person('유지민')
print(jimin.name)