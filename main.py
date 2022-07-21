# Устанавливаем Django в свежее виртуальное окружение:
# (venv) ~/django-projects $ pip3 install django
#
# И запускаем команду создания проекта:
# (venv) ~/django-projects $ django-admin startproject D2_9
#
# Запустим следующую команду, которая создаст новое приложение NewsPortal.
# (venv) ~/django-projects/D2_9 $ python3 manage.py startapp NewsPortal
#
# Теперь у нас проект django "D2_9", и приложение django "NewsPortal", всё в одном каталоге.
# В подкаталоге проекта "D2_9" есть файлы settyngs.py и urls.py, а в подкаталоге приложения "NewsPortal"
# файлы models.py, views.py, ......
# В файл models.py приложения market добавляем классы работы с базой данных для магазина.
# Потом создаём нужные миграции.
#
# (venv) ~/django-projects/D2_9 $ python3 manage.py makemigrations

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

if __name__ == '__main__':
    print('PyCharm')
