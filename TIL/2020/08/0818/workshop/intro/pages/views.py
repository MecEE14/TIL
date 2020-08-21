from django.shortcuts import render

# Create your views here.

def dinner(request, menu='메뉴', people='인원 수'):
    context = {
        'menu': menu,
        'people': people,
    }
    return render(request, 'dinner.html', context)