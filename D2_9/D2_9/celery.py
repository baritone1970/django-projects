import os
from celery import Celery

# связываем настройки Django с настройками Celery через переменную окружения DJANGO_SETTINGS_MODULE.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'D2_9.settings')

# создаем экземпляр приложения Celery и устанавливаем для него файл конфигурации.
# указываем пространство имен, чтобы Celery сам находил все необходимые настройки
# в общем конфигурационном файле settings.py. Он их будет искать по шаблону «CELERY_***».
app = Celery('D2_9')
app.config_from_object('django.conf:settings', namespace='CELERY')

# указываем Celery автоматически искать задания в файлах tasks.py каждого приложения проекта.
app.autodiscover_tasks()

#=========================================#
# согласно рекомендациям из документации к Celery, мы должны добавить следующие строки
# в файл __init__.py (рядом с settings.py):

#from .celery import app as celery_app
#__all__ = ('celery_app',)