# 우리편 탱커(전사, 암기, ...)
tanker_1_hp = 100
# 상대편 탱커(전사, 암기, ...)
tanker_2_hp = 100
# 이러면 방법이 없음

class Tanker:

    def __init__(self):
        self.hp = 100
        self.mp = 0
        
tanker1 = Tanker()
tanker2 = Tanker()
# 이러면 되죠~~
tanker1.hp = tanker1.hp - 20
print(tanker1.hp, tanker2.hp)