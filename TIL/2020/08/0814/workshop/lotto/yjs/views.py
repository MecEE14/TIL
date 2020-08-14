from random import sample
from django.shortcuts import render

# Create your views here.
def lotto(request):
    numbers = []
    for i in range(1, 46):
        numbers += [i]
    my_num = sample(numbers, 6)
    context = {
        'my_num': my_num
    }
    return render(request, 'lotto.html', context)