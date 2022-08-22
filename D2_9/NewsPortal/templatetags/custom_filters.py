# Здесь у нас фильтры для шаблонов, для файлов в каталоге /template с расширением .html

from django import template
import re

register = template.Library()       # А, понял, эта штука создаёт декоратор @register.filter() !!!

# Теперь используем декоратор @register.filter(), чтобы функция стала фильтром контента на страницах.
@register.filter()
def currency(value):
    """
    value: значение, к которому нужно применить фильтр
    """
    # Возвращаемое функцией значение подставится в шаблон.
    return f'{value} Р'

# А вот и цензор - фильтр замены запрещённых слов
@register.filter()
def censor(value):
   ToBeCensored=('да', 'нет')
   for pattern in ToBeCensored:
      value = re.sub(pattern, '***', value)
   return value
