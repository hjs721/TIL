# 키-값(key-value) 쌍으로 이뤄진 모음
# 키(key) : 불변 자료형만 가능(리스트, 딕셔너리 등은 불가능)
# 값(value) : 어떤 형태든 관계 없음
# 키와 값은 :로 구분됨. 개별 요소는 , 로 구분됨
# 변경 가능, 반복 가능

students = {"홍길동": 30, "김철수": 23}
print(students["홍길동"])  # 30
students["홍길동"] = 50
students["박영희"] = 95
print(students)  # {'홍길동': 50, '김철수': 23, '박영희': 95}
students.pop("홍길동")  # 존재하지 않는 키값을 넣을 경우 키에러 발생
print(students)  # {'김철수': 23, '박영희': 95}

movie = {
    "title": "설국열차",
    "genres": ["SF", "액션", "드라마"],
    "open-data": "2013-08-01",
    "time": 126,
    "adult": False,
}
print(movie["genres"])  # ['SF', '액션', '드라마']
