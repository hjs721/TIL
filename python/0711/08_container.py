name = "동현"
name1 = "효근"
name2 = "수경"
name3 = "나영"
name4 = "다겸"
name5 = "예지"

# 리스트
# 다양한 값들의 나열/시퀀스(순서대로)
students = ["동현", "효근", "수경", "나영", "다겸", "예지"]
# 인덱스(순서)로 접근
print(students[0])  # 동현
print(students[-1])  # 예지

students_1 = ["동현", "효근"]
students_2 = ["수경", "나영"]
students_3 = ["다겸", "예지"]

students = [["동현", "효근"], ["수경", "나영"], ["다겸", "예지"]]

# 딕셔너리 # 중괄호 # 키-값의 쌍
students = {"1회차": ["동현", "효근"], "2회차": ["수경", "나영"], "3회차": ["다겸", "예지"]}

# 접근할 때 키로 접근함
print(students["1회차"])
k = input()
print(students[f"{k}회차"])
