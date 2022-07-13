dust = int(input())
if dust > 150:
    print('매우 나쁨')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')


# if dust <= 30:
# elif dust > 30 and dust <= 80:
# elif dust > 80 and dust <= 150:
# else:
# 이것도 맞긴한데 위에가 훨씬 간단 (수학머리를 써보자...)