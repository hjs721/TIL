from django.shortcuts import render
import random

# Create your views here.

# View -> 템플릿 파일 지정
def index(request):
    return render(request, 'index.html')

def today_dinner(request):
    dinner_list = [
        {'menu': '떡볶이', 'src': 'https://pc9.kr/data/goods/1/2020/02/44_2020021815421615.jpg'},
        {'menu': '초밥', 'src': 'https://ichibankobe.com/ko/wdps/wp-content/uploads/2016/12/gankosushi07.jpg'},
        {'menu': '삼겹살', 'src': 'https://mp-seoul-image-production-s3.mangoplate.com/mango_pick/uker6u9xhkr1m8.jpg'},
        {'menu': '짜장면', 'src': 'https://i.ytimg.com/vi/Yn8ZFTBCJJQ/maxresdefault.jpg'},
        {'menu': '피자', 'src': 'https://ssproxy.ucloudbiz.olleh.com/v1/AUTH_e59809eb-bdc9-44d7-9d8f-2e7f0e47ba91/store16/11ada4b6a21384f7bf57c180852b141c_2726x2042.png'},
        {'menu': '치킨', 'src': 'https://img.siksinhot.com/place/1516858652943264.jpg'},
        {'menu': '찜닭', 'src': 'https://recipe1.ezmember.co.kr/cache/recipe/2015/08/15/58689dc18310020dec855f32c77079141.jpg'},
        {'menu': '라면', 'src': 'https://img.hankyung.com/photo/202007/99.18956024.1.jpg'},
        {'menu': '볶음밥', 'src': 'https://recipe1.ezmember.co.kr/cache/recipe/2015/07/13/3c7888976e35b583eab9d8d42f5a05e41_f.jpg'},
        {'menu': '파스타', 'src': 'https://t1.daumcdn.net/thumb/R1280x0/?fname=http://t1.daumcdn.net/brunch/service/user/4OhC/image/lNNoSaDd8uIQ6xTe_7txil9OR5E.jpg'}
    ]

    context = {
        'dinner' : random.choice(dinner_list)
    }
    return render(request, 'today_dinner.html', context)


def lotto(request):
    # lotto 번호 6개를 5번 뽑기(1부터 45)
    lotto_list = []
    for _ in range(5):
        lotto = random.sample(range(1, 46), 6)
        lotto_list.append(lotto)

    context = {
        'lotto_list': lotto_list
    }
    return render(request, 'lotto.html', context)