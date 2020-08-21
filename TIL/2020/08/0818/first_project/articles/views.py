# django imports style guide
# 1. standard library
# 2. 3rd party
# 3. Django
# 4. local django
import random
from datetime import datetime
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'articles/index.html')


def dinner(request):
    menus = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menus)
    context = {
        'pick': pick,
    }
    return render(request, 'articles/dinner.html', context)


def hello(request, name):
    context = {
        'name': name,
    }
    return render(request, 'articles/hello.html', context)


def dtl_practice(request):
    menus = ['짜장면', '탕수육', '짬뽕']
    fruits = ['banana', 'apple', 'pineapple', 'mango']
    my_sentence = 'Life is short, You need python'
    datetimenow = datetime.now()
    empty_list = []
    context = {
        'menus': menus,
        'empty_list': empty_list,
        'fruits': fruits,
        'my_sentence': my_sentence,
        'datetimenow': datetimenow,
    }
    return render(request, 'articles/dtl_practice.html', context)


def throw(request):
    return render(request, 'articles/throw.html')


def catch(request):
    # throw에서 보낸 form 데이터(requess.GET)를 받기
    message = request.GET.get('name')
    context = {
        'message': message,
    }
    return render(request, 'articles/catch.html', context)

