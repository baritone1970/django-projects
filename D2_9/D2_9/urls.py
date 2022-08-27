"""D2_9 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls.py import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls.py'))
"""
import django.contrib.flatpages.views
from django.contrib import admin
from django.urls import include, path, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),  # для автоматических страниц flatpages
    # Для аутентификации
    #    path('', include('protect.urls')),             # Это приложение я не делал
    #    path('sign/', include('sign.urls')),           # и это тоже. Попробую ограничиться allauth
    path('accounts/', include('allauth.urls')),  # это тоже файл из набора allauth, как у flatpages
    # Для отображения заголовка новостей или статей используем возможность include() дополнять **kwargs
    # https://django.fun/docs/django/ru/4.0/topics/http/urls/ - см. передача дополнительных параметров в include
    # 'header' - что показывать в заголовке, 'posttype' - что отбирать для показа, статьи или новости?
    path('news/', include('NewsPortal.urls'), {'header': 'Новости', 'posttype': 'NS'}),
    path('articles/', include('NewsPortal.urls'), {'header': 'Статьи', 'posttype': 'AR'}),
    # Эксперимент с отображением страниц с адресом, распознаваемым через регулярное выражение
    re_path(r'.*', django.contrib.flatpages.views.flatpage, kwargs={'url': '/doublecontent/'}),
]
