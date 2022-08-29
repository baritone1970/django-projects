from django_filters import FilterSet, DateTimeFilter
from django.forms import DateTimeInput
from .models import Post

# Создаем свой набор фильтров выдачи данных для модели Post.
# FilterSet - что-то вроде дженерика.
class NewsFilter(FilterSet):
    # класс FilterSet позволяет создавать фильтры через поля подкласса Meta
    # см. https://django-filter.readthedocs.io/en/stable/ref/filterset.html#automatic-filter-generation-with-model
    added_after = DateTimeFilter(
        field_name='time_of_creation',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )
    class Meta:
        model = Post # модель, в которой будем фильтровать записи.
        # В fields указывается, по каким полям модели будут работать создаваемые через Meta фильтры
        fields = {
            #    поиск по названию; по категории; позже указываемой даты.
            'header': ['contains'],
            'category': ['contains'],
            #'time_of_creation': ['date__gt'],
        }
