# 기본 순회에서는 key가 기준이고, 직접 딕셔너리에 key로 접근하면 value를 얻을 수 있다.
my_dict = {'apple': '사과', 'banana': '바나나'}

for word in my_dict:
    print(word, my_dict[word])


# 심화 형태
print(my_dict.keys()) # dict_keys(['apple', 'banana'])

print(my_dict.values()) # dict_values(['사과', '바나나'])
for value in my_dict.values():
    print(value)

print(my_dict.items()) # dict_items([('apple', '사과'), ('banana', '바나나')]) # 리스트 안에 튜플로 출력
for k, v in my_dict.items():
    print(k, v)

my_dict_2 = {}
my_dict_2['a'] = 'airplane'

my_dict_3 = {'a' : 0}
my_dict_3['a'] += 1
print(my_dict_3)