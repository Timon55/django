from .base import *

try:
    from .local import *
except ImportError:
    print('Ошибка импорта настроек из файла local, восстанови файл с помощью local.skelet !')