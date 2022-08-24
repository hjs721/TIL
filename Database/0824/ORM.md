# ORM

- Object-Relational-Mapping
- 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간의 데이터를 변환하는 프로그래밍 기술
- 파이썬에는 sQLAlchemy, peewee 등 라이브러리가 있으며 Django 프레임워크에서는 내장 Django ORM을 사용

"객체(object)로 DB를 조작한다."

```python
Genre.objects.all()
```

```sqlite
SELECT * FROM Genre;
```

- 모델 설계

```python
class Genre(models.Model):
    name = models.CharField(max_length = 30)
```

