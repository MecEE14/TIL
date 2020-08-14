import random
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')


# 1번 menu 함수 만들기,
def menu(request):
    # 2번 메뉴 3개가 들어간 리스트 만들기
    menus = ['짜장', '짬뽕', '치킨']
    # 3번 그 중 메뉴 하나를 random으로 뽑아서 변수에 저장하고
    pick = random.choice(menus)
    context = {
        'pick': pick,
        'menus': menus,
    }
    return render(request, 'menu.html', context)

