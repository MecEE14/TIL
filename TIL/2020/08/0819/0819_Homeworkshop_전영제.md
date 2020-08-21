# 0819_Homeworkshop_전영제

## Homework

### prob 1

```
migration
pyhton manage.py makemigration
pyhton manage.py migrate
pyhton manage.py sqlmigrate
pyhton manage.py showmigrations
```

### prob 2



### prob 3

```
python manage.py shell(_plus)
```

### prob 4

```
id, title, content, create_at, update_at
```



## Workshop

### 1. intro/settings.py

```
'DIRS': [BASE_DIR/'intro'/'templates']
INSTALLED_APPS = [
    'pages',
    ]
```

### 2. intro/urls.py

```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('pages.urls'))
]
```

### 3. pages/views.py

```
from django.shortcuts import render

# Create your views here.

def card(request):
    articles = [
    ['test title1', 'test content1'],
    ['test title2', 'test content2'],
    ['test title3', 'test content3'],
    ['test title4', 'test content4'],
    ['test title5', 'test content5'],
    ]
    context = {
        'articles': articles
    }
    return render(request, 'pages/card.html', context)

def community(request):
    articles2 = [
    ['#', 'Title', 'Content', 'Creation Time'],
    ['test title 1', 'test content 1', 'test creation time1'],
    ['test title 2', 'test content 2', 'test creation time2'],
    ['test title 3', 'test content 3', 'test creation time3'],
    ['test title 4', 'test content 4', 'test creation time4'],
    ['test title 5', 'test content 5', 'test creation time5'],
    ['test title 6', 'test content 6', 'test creation time6'],
    ]
    context = {
        'articles2': articles2,
    }
    return render(request, 'pages/community.html', context)
```

### 4. intro/templates/base.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
  <title>{% block title %}BASE{% endblock %}</title>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <a class="navbar-brand" href="#">Articles</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>
    <div class="container">
    <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
        <li class="nav-item">
            <a class="nav-link" href="{% url 'pages:card' %}">Card <span class="sr-only">(current)</span></a>
        </li>
        <li class="nav-item">
            <a class="nav-link" href="{% url 'pages:community' %}">Community</a>
        </li>
        </ul>
    </div>
    </div>
    </nav>
    {% block content %}
    {% endblock %}
  <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>
</body>
</html>
```

### 5. pages/templates/card.html

```html
{% extends 'base.html' %}
{% block title %}
pages/card
{% endblock  %}
{% block content %}
{% for arty in articles %}
    <div class='container'>
        <div scope="col">
            <div class="card" style="width: 18rem;">
            <img class="card-img-top" src="https://picsum.photos/200/300" alt="Card image cap">
            <div class="card-body">
                <h5 class="card-title">{{ arty.0 }}</h5>
                <p class="card-text">{{ arty.1 }}</p>
                <a href="{% url 'pages:community' %}" class="btn btn-primary">Post Article</a>
            </div>
            </div>
        </div>
    </div>
{% endfor %}
{% endblock  %}
```

### 6. pages/templates/community.html

``` html
{% extends 'base.html' %}
{% block title %}
pages/community
{% endblock  %}
{% block content %}
    <table class="table">
    {% for arty in articles2 %}
    {% if forloop.first %}
        <thead>
            <tr>
            <th scope="col">{{arty.0 }}</th>
            <th scope="col">{{arty.1 }}</th>
            <th scope="col">{{arty.2 }}</th>
            <th scope="col">{{arty.3 }}</th>

            </tr>
        </thead>
    {% else %}
        <tbody>
            <tr>
            <th scope="row">{{forloop.counter0}}</th>
            <td>{{arty.0 }}</td>
            <td>{{arty.1 }}</td>
            <td>{{arty.2 }}</td>
            </tr>
        </tbody>
    {% endif %}
  {% endfor %}

</table>
{% endblock  %}
```

