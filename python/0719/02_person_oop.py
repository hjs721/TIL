class Person:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def info(self):
        return(self.name, self.age, self.gender)

hong = Person('홍길동', 100, 'M')
ko = Person('고길동', 10, 'M')

print(hong.info())
print(hong.name)
print(hong.age)
print(type(hong))
print(ko.info())

# 클래스는 Person이고, List
# 인스턴스는 홍길동이고, ['홍길동', 100, 'M'] < 각각의 개별 사례