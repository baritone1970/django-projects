from django.shortcuts import render

# Create your views here.
from datetime import datetime
from django.urls import reverse, reverse_lazy  # TODO D4.5, используется в удалении постов, зачем не понял
# На ListView делаем список новостей, на DetailView - показ публикаций, и, возможно, авторов
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Post, User, Author  # Класс Post, который мы определили в файле models.py
from .filters import NewsFilter
from .forms import PostForm


def news(request):
    return HttpResponse("<h1>Breaking news!!</h1>")


class PostList(ListView):
    # Сюда можно передать дополнительный аргумент через path(), сейчас это header='Список новостей'
    model = Post
    ordering = '-time_of_creation'  # Поле для сортировки объектов, "-blabla" - обратный отсчёт
    template_name = 'posts.html'
    context_object_name = 'posts'  # Имя списка, через который обращаются ко всем объектам в html-шаблоне.
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
        # Отбираем для показа статьи или новости
        # if self.request.path == '/article/':
        #    posttype=Post.POST_TYPE[0][0]#(type='AR')
        # else # '/news/'
        #    posttype = Post.POST_TYPE[1][0]#(type='NS')
        # Или лучше задавать в urls.py через **kwargs, чтобы не забыть и не запутаться в имеющихся типах постов?
        # https://django.fun/docs/django/ru/4.0/topics/http/urls/
        posttype = self.kwargs['posttype']
        # Получаем запрос нужного типа постов, но без фильтров из filters.py
        queryset = super().get_queryset().filter(type=posttype)
        # Используем наш класс фильтрации.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        # Для фильтрации queryset предназначен django-filter
        # https://django-filter.readthedocs.io/en/stable/guide/usage.html#
        # self.request.GET содержит объект QueryDict, см. D4.2.2
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
        context['path'] = self.request.path
        # **kwargs передаётся в класс из url.py верхнего уровня через path() ?
        # https://django.fun/docs/django/ru/4.0/topics/http/urls/
        context['header'] = self.kwargs['header']  # .items()# .values() #
        #
#        context['post_author'] = self.get_queryset().get(post_author=str(self.request.user))#
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post_detail'


class PostSearch(ListView):
    model = Post
    ordering = '-time_of_creation'  # Поле для сортировки объектов, "-blabla" - обратный отсчёт
    template_name = 'post_search.html'
    context_object_name = 'posts'  # Имя списка, через который обращаются ко всем объектам в html-шаблоне.
    paginate_by = 2  # TODO - разобраться с переходом к следующей странице при пажинации
    def get_queryset(self):
        posttype = self.kwargs['posttype']
        queryset = super().get_queryset().filter(type=posttype)
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['path'] = str(self.request.path).removesuffix('search/')
        context['header'] = self.kwargs['header']  # .items()# .values() #
        #context['post_author'] = Author.#.get(post_author=self.request.user)#self.get_queryset().get(post_author=self.request.user)#
        #Exception Type:	ValueError   # self.request.user - имя пользователя
        #Exception Value:	Field 'id' expected a number but got 'AnonymousUser'.
        context['filterset'] = self.filterset
        return context



class PostCreate(CreateView):  # TODO D4.5
    # Указываем нашу разработанную форму
    form_class = PostForm
    # модель со списком постов
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'post_edit.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление ' + str(self.kwargs['header']).lower()  # 'Добавление поста'
        #        context['menu'] = menu
        context['posttype'] = self.kwargs['posttype']
        return context


class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование ' + str(self.kwargs['header']).lower()  # 'Редактирование поста'
        #        context['menu'] = menu
        context['posttype'] = self.kwargs['posttype']
        return context


class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('news')  # TODO D4.5
# В представлении удаления мы также не указываем форму.
# Вместо неё появляется поле success_url, в которое мы должны указать,
# куда перенаправить пользователя после успешного удаления товара.
# Логика работы reverse_lazy() точно такая же, как и у функции reverse, которую мы использовали в модели Product.

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удаление ' + str(self.kwargs['header']).lower()  # 'Удаление поста'
        #        context['menu'] = menu
        context['posttype'] = self.kwargs['posttype']
        return context
