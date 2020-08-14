# 0814 homeworkshop 전영제

## homeworkshop

### prob 1

```
TIME_ZONE = 'UTC' 에서 UTC를 Asia-Seoul로 바꿔준다.
```



### prob 2

```
'ssafy/', views.ssafy
```



### prob 3

#### 1

```html
{% for items in menu %}
    {{items}}
{% endfor %}
```



#### 2

``` html
    {% for post in posts %}
        {{forloop.counter}}번 글 : {{post}}
    {% endfor %}
```



#### 3

``` html
    {% for user in users %}
        {{ user }} 명
    {% empty %}
        현재 가입한 유저가 없습니다.
    {% endfor %}
```



#### 4

```

```



#### 5

``` html
    {{'hello'|length}}
    {{'my name is tom'|title}}
```



#### 6

```

```



### prob 4

### 1

> form에서 입력이 끝났을 때 이동할 주소

#### 2

> title, content, my-site

#### 3

> /creat/?title=안녕하세요&content=반갑습니다&my-site=파이팅





## workshop

#### 1. intro/urls.py

``` html
from django.contrib import admin
from django.urls import path
from yjs import views

urlpatterns = [
    path('lotto/', views.lotto),
    path('admin/', admin.site.urls),
]
```



#### 2. pages/views.py

``` html
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
```



#### 3. template/lotto.html

``` html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>제 OOO회 로또 번호 추천</h1>
    <h4>SSAFY님께서 선택하신 로또 번호는 {{my_num}}입니다.</h4>
</body>
</html>
```



