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
# Для запуска сервера используем команду в консоли:
# (venv) ~/django-projects/D2_9 $ python manage.py runserver
#
# Чтобы получить доступ к django shell:
# (venv) ~/django-projects/D2_9 $ python manage.py shell

