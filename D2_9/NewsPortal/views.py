from django.shortcuts import render

# Create your views here.
from datetime import datetime
from django.urls import reverse_lazy # TODO D4.5, используется в удалении постов, зачем не понял
# На ListView делаем список новостей, на DetailView - показ публикаций, и, возможно, авторов
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Post  # Класс Post, который мы определили в файле models.py
from .filters import NewsFilter
from .forms import PostForm


def news(request):
    return HttpResponse("<h1>Breaking news!!</h1>")


class NewsList(ListView):
    model = Post
    ordering = '-time_of_creation'  # Поле для сортировки объектов, "-blabla" - обратный отсчёт
    template_name = 'posts.html'
    context_object_name = 'news'  # Имя списка, через который обращаются ко всем объектам в html-шаблоне.
    paginate_by = 2  # TODO - разобраться с переходом к следующей странице при пажинации

    # наследуется метод .as_view(), переопределяем get_queryset() и get_context_data()
    # Можно ещё что-то с get_object() поделать, но вроде не обязательно.
    # Смотрим

    # TODO - ещё не понял, как разобраться с сортировкой только новостей!
    # При отображении списка всех объектов ListView по умолчанию возвращает Model.objects.all()
    # Вот здесь показано, как фильтровать выдачу через переопределение  get_queryset()
    # https://django.fun/docs/django/ru/4.0/topics/db/managers/
    # Здесь пока переопределяем функцию получения списка товаров
    # с целью добавления внешнего фильтра, и больше ничего.
    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = NewsFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    # Метод get_context_data позволяет изменить набор данных, который будет передан в шаблон.
    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами,
        # что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        context['time_now'] = datetime.utcnow()
        # Для анализа пути, по которому вызвали страницу,
        # чтобы решить, что отображать - новости или статьи.....
        context['request'] = self.request.path
        # Добавляем в контекст объект фильтрации. TODO Как это действует - не понял
        context['filterset'] = self.filterset
        return context


class NewsDetail(DetailView):
    model = Post
    template_name = 'newsdetail.html'
    context_object_name = 'newsdetail'

class PostSearch(ListView):
    model = Post
    ordering = '-time_of_creation'  # Поле для сортировки объектов, "-blabla" - обратный отсчёт
    template_name = 'post_search.html'
    context_object_name = 'post_found'  # Имя списка, через который обращаются ко всем объектам в html-шаблоне.
    paginate_by = 2  # TODO - разобраться с переходом к следующей странице при пажинации

class PostCreate(CreateView):   #TODO D4.5
    # Указываем нашу разработанную форму
    form_class = PostForm
    # модель со списком постов
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'post_edit.html'
#    success_url = reverse_lazy('news')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление статьи'
#        context['menu'] = menu
        return context

class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('news') #TODO D4.5
# В представлении удаления мы также не указываем форму.
# Вместо неё появляется поле success_url, в которое мы должны указать,
# куда перенаправить пользователя после успешного удаления товара.
# Логика работы reverse_lazy() точно такая же, как и у функции reverse, которую мы использовали в моделе Product.