# import sys
from django.db import models

# Genre 클래스를 만드는데,
# models.Model 내부 클래스를 상속받는다.
# Q. 왜 상속받을까요? A. 미리 만들어진 기능들을 활용하고 싶어서

# class Genre(models.Model):
#     name = models.CharField(max_length = 30)

# class Person:
#     pass

# # iu라고 하는 변수의 이름을 가진 Person 클래스의 인스턴스를 만드는 코드는?
# iu = Person()
# # iu의 name 속성으로 아이유라고 하는 코드는?
# iu.name = '아이유'

# class Artists(models.Model):
#     name = models.CharField(max_length = 30)
#     debut = models.DateField()

class Director(models.Model):
    name = models.TextField()
    debut = models.DateTimeField()
    country = models.TextField()

class Genre(models.Model):
    title = models.TextField()

import datetime
# Director.objects.create(name='봉준호', debut=datetime.date(1993, 1, 1), country='KOR')
# Director.objects.create(name='최동훈', debut=datetime.date(2004, 1, 1), country='KOR')
# Director.objects.create(name='이정재', debut=datetime.date(2022, 1, 1), country='KOR')
# Director.objects.create(name='이경규', debut=datetime.date(1992, 1, 1), country='KOR')
# Director.objects.create(name='한재림', debut=datetime.date(2005, 1, 1), country='KOR')
# Director.objects.create(name='Joseph Kosinski', debut=datetime.date(1999, 1, 1), country='KOR')
# Director.objects.create(name='김철수', debut=datetime.date(2022, 1, 1), country='KOR')

# genre = Genre()
# genre.title = '액션'
# genre.save()
# genre = Genre()
# genre.title = '드라마'
# genre.save()
# genre = Genre()
# genre.title = '사극'
# genre.save()
# genre = Genre()
# genre.title = '범죄'
# genre.save()
# genre = Genre()
# genre.title = '스릴러'
# genre.save()
# genre = Genre()
# genre.title = 'SF'
# genre.save()
# genre = Genre()
# genre.title = '무협'
# genre.save()
# genre = Genre()
# genre.title = '첩보'
# genre.save()
# genre = Genre()
# genre.title = '재난'
# genre.save()

# directors = Director.objects.all()
# for director in directors:
#     print(director.name, director.debut, director.country)

# director = Director.objects.get(id=1)
# print(director.name, director.debut, director.country)

# directors = Director.objects.filter(country='KOR')
# for director in directors:
#     print(director.name, director.debut, director.country)

# director = Director.objects.get(name='Joseph Kosinski')
# director.country = 'USA'
# director.save()
# print(director.name, director.debut, director.country)

# director = Director.objects.get(name='김철수')
# director.delete()