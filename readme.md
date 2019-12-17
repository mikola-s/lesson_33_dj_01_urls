## ДЗ на урок 33

### задание:

#### Создаем 3 разных приложение:
- News;
- Article;
- Comments.

#### У всех троих должны быть раличные типы урлов:
##### 1 уровень - статические урлы;
- /new
- /edit
- /lock

##### 2 уровень - динамические урлы;
- /<id>/
- /<id>/add
- /<id>/delete

##### 3 уровень -  сложные урлы:
- /nnsss/, где n - номер, s - буква
- /n-s-n/
- /099-602-52-41/

И надо, чтобы на сайт вывели данную информацию.



### выполнение:

#### создал проекта

```
~$ python3 -m venv .venv
~$ source .venv/bin/activate
(.venv)~$ pip install django==2.2
(.venv)~$ django-admin startproject lsn33_home_work
(.venv)~$ pip freeze > requirement.txt
```

#### создал приложений

```
(.venv)~/lsn33_home_work/$ ./manage.py startapp news
(.venv)~/lsn33_home_work/$ ./manage.py startapp article
(.venv)~/lsn33_home_work/$ ./manage.py startapp comments

```

#### создал в приложениях файлы urls.py

```
(.venv)~/lsn33_home_work/$ touch news/urls.py
(.venv)~/lsn33_home_work/$ touch article/urls.py
(.venv)~/lsn33_home_work/$ touch comments/urls.py
```


#### структура проекта

<details> 
    <summary>(спойлер)</summary>
    
```
├── article
│   ├── migrations
│   │   └── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── comments
│   ├── migrations
│   │   └── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── news
│   ├── migrations
│   │   └── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── lsn33_home_work
│   ├── __init__.py
│   ├── settings.py
│   ├── lsn33_home_work
│   └── wsgi.py
├── manage.py
└── db.sqlite3

```
</details>

#### вписал URL приложений в файл lsn33_home_work/urls.py

```python

from django.contrib import admin
from django.urls import path, include


urlpatterns = {
    path('admin/', admin.site.urls),
    path('news/', include("news.urls")),
    path('article/', include("article.urls")),
    path('comments/', include("comments.urls")),
}

```

#### вписал URL представелений в файле news/urls.py 

```python

from django.urls import path, re_path
from . import views

urlpatterns = [
    # level 01
    path('', views.base),
    path('new/', views.new),
    path('edit/', views.edit),
    path('lock/', views.lock),

    # level 02
    path('<int:id>/', views.id_base),
    path('<int:id>/add', views.id_add),
    path('<int:id>/delete', views.id_delete),

    # level 03
    re_path(r'^(?P<page>\d{2}[A-z]{3})/$', views.any_right),
    re_path(r'^(?P<page>\d-[A-z]-\d)/$', views.any_right),
    re_path(r'^(?P<page>(050|066|095|099|039|067|068|096|097|098|063|093|091|092|094)-\d{3}(-\d\d){2})/$',
            views.any_right),
]

```

#### создал представеления в файле news/views.py

```python

from django.http import HttpResponse


# level 01
def base(request):
    response = HttpResponse(f'You got to the page {str(request.path)} </br> '
                            f'It is "{str(request.path).split("/")[1]}" base page')
    return response


def new(request):
    response = HttpResponse(f'You got to the page {str(request.path)} </br> '
                            f'It is "new" in "{str(request.path).split("/")[1]}" page')
    return response


def edit(request):
    response = HttpResponse(f'You got to the page {str(request.path)} </br> '
                            f'It is "edit" in "{str(request.path).split("/")[1]}" page')
    return response


def lock(request):
    response = HttpResponse(f'You got to the page {str(request.path)} </br> '
                            f'It is "lock" in "{str(request.path).split("/")[1]}" page')
    return response

# level 02


def id_base(request, id):
    response = HttpResponse(f'You got to the page {str(request.path)} </br> '
                            f'It is ID={id} base page in "{str(request.path).split("/")[1]}" page')
    return response


def id_add(request, id):
    response = HttpResponse(f'You got to the page {str(request.path)} </br> '
                            f'It is "{id}.add"  in "{str(request.path).split("/")[1]}" page')
    return response


def id_delete(request, id):
    response = HttpResponse(f'You got to the page {str(request.path)} </br> '
                            f'It is "{id}.base" page in "{str(request.path).split("/")[1]}" page')
    return response


# level 03

def any_right(request, page):
    response = HttpResponse(f'You got to the page {str(request.path)} </br> '
                            f'It is "{page}" in "{str(request.path).split("/")[1]}" page')
    return response

```

#### импортировал views.py и urls.py в приложения article и comments

<details open="open">
    <summary> файл comments/urls.py и article/urls.py </summary>
    
    
```python

from . import views
from news import urls

urlpatterns = urls.urlpatterns

```
</details>

<details open="open">
    <summary> файл comments/views.py и article/views.py </summary>
    
    
```python

from news import views

```
</details>

---------------------------------

[ссылка на папку проекта](https://github.com/mikola-s/lesson_33_dj_01_urls/tree/master/lsn33_home_work)