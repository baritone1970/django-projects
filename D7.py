# D7.2
# (virtualenv) $ pip3 install celery
# Перейти в директорию проекта и добавить файл celery.py рядом с settings.py, добавить настройки
# потом добавить настройки в __init__.py
# D7.3
# Потом установить Redis (см. так же C5.5)
# $> emerge dev-db/redis
# Удостовериться в том, что Redis установлен, можно с помощью команды:
# $> redis-cli ping
# Если нет ответа PONG, вероятно, сервер не запущен, и надо запустить его командой
# $ redis-server
# Затем перенастроить библиотеки в виртуальном окружении Python
# (virtualenv) $ pip3 install redis
# (virtualenv) $ pip3 install -U "celery[redis]"
# Затем в конфигурацию проекта (settings.py) дописываются несколько переменных (см. настройки celery.py, D7.3).
# Проверка - запуском одновременно, в фоне или в разных терминалах, сервера джанго и cellery
# (virtualenv) $ python3 manage.py runserver
# (virtualenv) $ celery -A D2_9 worker -l INFO
