'''
добавьте в settings.py следующую строку:

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]
подключить LocaleMiddleware в настройках:
MIDDLEWARE = [
.......
'django.contrib.sessions.middleware.SessionMiddleware',
'django.middleware.locale.LocaleMiddleware',    # Здесь!
'django.middleware.common.CommonMiddleware',
...................
]
'''