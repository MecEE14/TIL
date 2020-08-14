from django.utils import timezone
from django.shortcuts import render

# Create your views here.

def prob1(request):
    menu = ['성게알초밥', '스테이크', '파스타']
    context = {
        'menu': menu
    }
    return render(request, 'prob1.html', context)

def prob2(request):
    posts = ['1번가', '3번가', '7번가', '11번가']
    context = {
        'posts': posts
    }
    return render(request, 'prob2.html', context)

def prob3(request):
    users = []
    context = {
        'users': users
    }
    return render(request, 'prob3.html', context)

def prob4(request):
    menu = ['성게알초밥', '스테이크', '파스타']
    context = {
        'menu': menu
    }
    return render(request, 'prob4.html', context)

def prob5(request):
    return render(request, 'prob5.html')

def prob6(request):
    today = timezone.localtime()
    context = {
        'today': today
    }
    return render(request, 'prob6.html', context)