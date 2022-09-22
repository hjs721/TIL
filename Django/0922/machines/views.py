from django.shortcuts import render
import random

# Create your views here.

def dinner(request):
    # 메뉴
    menus = ['삼겹살', '마라탕', '국밥', '짜장면', '라면', '초밥', '떡볶이', '볶음밥']

    menu_index = menus.index(random.choice(menus))

    menu = menus[menu_index]
    
    # 이미지
    images = ['https://cdn.wadiz.kr/wwwwadiz/green001/2020/0731/20200731125659031_73846.png/wadiz/format/jpg/quality/80/optimize',
    'https://ssproxy.ucloudbiz.olleh.com/v1/AUTH_e59809eb-bdc9-44d7-9d8f-2e7f0e47ba91/uploads/ds_20417_1629871099VQqBFMr.jpg',
    'https://t1.daumcdn.net/liveboard/HYPEBEAST/69f4177fb78a40ddad49e33d4b186940.JPG',
    'https://www.tsunagulocal.com/wp-content/uploads/2020/08/IMG_8956-scaled.jpg',
    'https://cphoto.asiae.co.kr/listimglink/1/2020110410540482196_1604454845.jpg',
    'https://img.siksinhot.com/place/1520903294848009.jpg',
    'https://t1.daumcdn.net/thumb/R1280x0/?fname=http://t1.daumcdn.net/brunch/service/user/5dJg/image/hX1as7-w6AcGNZ72wDIl5agWU3k.jpg',
    'https://recipe1.ezmember.co.kr/cache/recipe/2015/07/13/3c7888976e35b583eab9d8d42f5a05e41_f.jpg'
    ]
    image = images[menu_index]
    context = {
        'menu': menu,
        'img': image
    }
    return render(request, 'dinner.html', context)

def lotto(request):

    number = random.sample(range(1, 46), 6)
    context = {
        'lotto' : number
    }
    return render(request, 'lotto.html', context)