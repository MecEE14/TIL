# 0818_Homeworkshop_전영제

## Homework

### prob 1

| MTV      | MVC        |
| -------- | ---------- |
| Model    | Model      |
| Template | View       |
| View     | Controller |



### prob 2

```
Variable Routing
```



### prob 3

```
templates
```



### prob 4

> 정적 웹 페이지 (static web page)

- 서버에 미리 저장된 파일이 그대로 전달되는 웹 페이지
- 서버는 사용자가 보낸 요청에 해당하는 웹 페이지를 보냄



> 동적 웹 페이지 (dynamic web page)

- 서버에 있는 데이터들을 스크립트에 의해 가공처리한 후 생성되어  전달되는 웹 페이지
- 서버는 사용자의 요청을 해석하여 데이터를 가공한 후 생성되는 웹 페이지를  보냄



## Workshop

### 1. intro/urls.py

```html
from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dinner/<str:menu>/<int:people>/', views.dinner),
]
```

### 2. pages/views.py

```
def dinner(request, menu='메뉴', people='인원 수'):
    context = {
        'menu': menu,
        'people': people,
    }
    return render(request, 'dinner.html', context)
```

### 3. templates/dinner.html

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>저녁 메뉴</h1>
    <p>저녁 먹을 사람?! {{ people }} 명</p>
    <p>어떤 메뉴?! {{ menu }}</p>
</body>
</html>
```



