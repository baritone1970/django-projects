from django.shortcuts import render

# Create your views here.
from datetime import datetime
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import Post    # Класс Post, который мы определили в файле models.py
from .filters import NewsFilter

def news(request):
    return HttpResponse("<h1>Breaking news!!</h1>")

class NewsList(ListView):
   model = Post
   ordering = '-time_of_creation'    # Поле для сортировки объектов, "-blabla" - обратный отсчёт
   template_name = 'news.html'
   context_object_name = 'news'   # Имя списка, через который обращаются ко всем объектам в html-шаблоне.
   paginate_by = 10 #TODO - разобраться с переходом к следующей странице при пажинации

   # наследуется метод .as_view()

#TODO - ещё не понял, как разобраться с сортировкой только новостей!
   # Переопределяем функцию получения списка товаров
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
       # Добавляем в контекст объект фильтрации.
       context['filterset'] = self.filterset
       return context


class NewsDetail(DetailView):
   model = Post
   template_name = 'newsdetail.html'
   context_object_name = 'newsdetail'
