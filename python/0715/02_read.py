# 파일명, 어떤 모드로 열지, 인코딩 설정
with open('students.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    print(text, type(text))
    names = text.split()  # ==> list 타입. 이러면 길이를 구할 수도 있고 내용을 분석할 수도 있겠죠
    cnt = 0
    for name in names:
        # name : 첫번째 시행 - 김세환
        if name[0] == '김':
        # if name.startswith('김') 이것도 같은 코드. 시각적으로는 이쪽이 더 명확함
            cnt += 1
    print(cnt)