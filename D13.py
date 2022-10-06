'''
Итоговое задание 13.4
Настоящие системы логирования очень распределенные и орудуют большим количеством связанных компонентов.
Давайте попробуем создать подобный механизм. Ваши настройки логирования должны выполнять следующее:

1) В консоль должны выводиться все сообщения уровня DEBUG и выше, включающие время, уровень сообщения, сообщения.
   Для сообщений WARNING и выше дополнительно должен выводиться путь к источнику события
   (используется аргумент pathname в форматировании). А для сообщений ERROR и CRITICAL еще должен выводить стэк ошибки
   (аргумент exc_info). Сюда должны попадать все сообщения с основного логгера django.
2) В файл general.log должны выводиться сообщения уровня INFO и выше только с указанием
   времени, уровня логирования, модуля, в котором возникло сообщение (аргумент module) и само сообщение.
   Сюда также попадают сообщения с регистратора django.
3) В файл errors.log должны выводиться сообщения только уровня ERROR и CRITICAL. В сообщении указывается
   время, уровень логирования, само сообщение, путь к источнику сообщения и стэк ошибки.
   В этот файл должны попадать сообщения только из логгеров
   django.request, django.server, django.template, django.db_backends.
4) В файл security.log должны попадать только сообщения, связанные с безопасностью, а значит только из
   логгера django.security. Формат вывода предполагает время, уровень логирования, модуль и сообщение.
5) На почту должны отправляться сообщения уровней ERROR и выше из django.request и django.server по формату,
   как в errors.log, но без стэка ошибок.
Более того, при помощи фильтров нужно указать, что в консоль сообщения отправляются только при DEBUG = True,
а на почту и в файл general.log — только при DEBUG = False.
'''