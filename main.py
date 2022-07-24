# Устанавливаем Django в свежее виртуальное окружение:
# (venv) ~/django-projects $ pip3 install django
#
# И запускаем команду создания проекта:
# (venv) ~/django-projects $ django-admin startproject D2_9
#
# Запустим следующую команду, которая создаст новое приложение NewsPortal.
# (venv) ~/django-projects/D2_9 $ python manage.py startapp NewsPortal
#
# Теперь у нас проект django "D2_9", и приложение django "NewsPortal", всё в одном каталоге.
# В подкаталоге проекта "D2_9" есть файлы settyngs.py и urls.py, а в подкаталоге приложения "NewsPortal"
# файлы models.py, views.py, ......
# Создаём нужные миграции.
# (venv) ~/django-projects/D2_9 $ python manage.py makemigrations
#
# Применяем миграции к базе данных
# (venv) ~/django-projects/D2_9 $ python manage.py migrate
#
# Чтобы получить доступ к django shell:
# (venv) ~/django-projects/D2_9 $ python manage.py shell

# В консоли Django надо:
# 1) Создать двух пользователей (с помощью метода User.objects.create_user('username')).
# 2) Создать два объекта модели Author, связанные с пользователями.
# 3) Добавить 4 категории в модель Category.
# 4) Добавить 2 статьи и 1 новость.
# 5) Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).
# 6) Создать как минимум 4 комментария к разным объектам модели Post
#    (в каждом объекте должен быть как минимум один комментарий).
# 7) Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.
# 8) Обновить рейтинги пользователей.
# 9) Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).
# 10) Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи,
#     основываясь на лайках/дислайках к этой статье.
# 11) Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.

from django.contrib.auth.models import User
from D2_9.NewsPortal.models import *

# Создание двух пользователей (с помощью метода User.objects.create_user('username')).
u1 = User.objects.create_user('u1')
u2 = User.objects.create_user('u2')
# Создание двух объектов модели Author, связанных с пользователями.
a1 = Author.objects.create(id_user=u1)
a2 = Author.objects.create(id_user=u2)
# Добавление 4 категорий в модель Category.
c1 = Category.objects.create(name="Категория1")
c2 = Category.objects.create(name="Категория2")
c3 = Category.objects.create(name="Категория3")
c4 = Category.objects.create(name="Категория4")
# Добавление 2 статей и 1 новости.
post1 = Post.objects.create(id_author=a1, type=Post.article, header="Статья 1", text="Текст статьи 1", rating=0)
post2 = Post.objects.create(id_author=a2, type=Post.article, header="Статья 2", text="Текст статьи 2", rating=0)
post3 = Post.objects.create(id_author=a1, type=Post.news, header="Новость 1", text="Текст новости 1", rating=0)
# Присвоение им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).
PostCategory.objects.create(id_post=post1, id_category=c4)
PostCategory.objects.create(id_post=post2, id_category=c1)
PostCategory.objects.create(id_post=post2, id_category=c2)
PostCategory.objects.create(id_post=post3, id_category=c3)
# Создание как минимум 4 комментария к разным объектам модели Post
comment1 = Comment.objects.create(id_post=post1, id_user=u1, text="Комментарий пользователя 1 к статье 1", rating=0)
comment2 = Comment.objects.create(id_post=post2, id_user=u2, text="Комментарий пользователя 2 к статье 2", rating=0)
comment3 = Comment.objects.create(id_post=post3, id_user=u1, text="Комментарий пользователя 1 к новости 1", rating=0)
comment4 = Comment.objects.create(id_post=post3, id_user=u2, text="Комментарий пользователя 2 к новости 1", rating=0)
# Скорректировать рейтинги этих статей и новостей функциями like() и dislike()
post1.like()
post1.like() # Итоговый рейтинг +2 статье 1
post2.like() # Итоговый рейтинг +1 статье 2
post3.dislike()
post3.like()
post3.dislike() # Итоговый рейтинг -2 новости 1
# 8) Обновить рейтинги пользователей (вернее, авторов).
a1.update_rating()
a2.update_rating()
# 9) Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).
# 10) Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи,
#     основываясь на лайках/дислайках к этой статье.
# 11) Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.
