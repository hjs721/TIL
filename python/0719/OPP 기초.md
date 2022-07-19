```# 클래스 정의
Class Myclass:
    pass
# 인스턴스 생성
my_instance = MyClass()
# 메서드 호출
my_instance.my_method()
# 속성
my_instance.my_attribute```

roTtenapPle
rottenApple

sn_ake_case
snake_case

# 클래스와 인스턴스
- 클래스 : 객체들의 분류(class)
- 인스턴스 : 하나하나의 실체/예(instance)

# 인스턴스 메소드
- 호출 시, 첫번째 인자로 인스턴스 자기자신(self)이 전달됨
# self
- 인스턴스 자기 자신
- 파이썬에서 인스턴스 메소든는 호출 시 첫번째 인자로 인스턴스 자신이 전달되게 설계됨
-- 매개변수 이름으로 self를 첫번째 인자로 정의
-- 다른 단어로 써도 작동하지만, 파이선의 암묵적인 규칙

# 생성자(constructor) 메소드
- 인스턴스 객체가 생성될 때 자동으로 호출되는 메소드
- 인스턴스 변수들의 초기값을 설정
-- 인스턴스 생성
-- __init__