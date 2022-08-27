from django_filters import FilterSet
from .models import Post

# Создаем свой набор фильтров выдачи данных для модели Post.
# FilterSet - что-то вроде дженерика.
class NewsFilter(FilterSet):
   class Meta:
       # В Meta классе мы должны указать Django модель,
       # в которой будем фильтровать записи.
       model = Post
       # В fields мы описываем по каким полям модели
       # будет производиться фильтрация.
       fields = {
           # поиск по названию,
           #    * по названию;
           #    * по категории;
           #    * позже указываемой даты.
           'header': ['icontains'],
           'category': ['icontains'],
           'time_of_creation': [],
       }