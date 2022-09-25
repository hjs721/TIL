"""practice_0923 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from random_machine import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 1. path 등록
    # '' 비워두면 루트 주소
    # 2. 어떤 view를 실행할지 지정
    path('', views.index),
    path('today-dinner/', views.today_dinner),
    path('lotto/', views.lotto),
]
