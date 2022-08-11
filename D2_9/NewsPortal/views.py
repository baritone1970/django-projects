from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import Post    # Класс Post, который мы определили в файле models.py
from .filters import NewsFilter

def news(request):
    return HttpResponse("<h1>Breaking news!!</h1>")

class NewsList(ListView):
   model = Post
   ordering = 'time_of_creation'    # Поле, которое будет использоваться для сортировки объектов
   template_name = 'news.html'
    # Его надо указать, чтобы обратиться к списку объектов в
   context_object_name = 'news'   # Имя списка, через который обращаются ко всем объектам в html-шаблоне.
   paginate_by = 2

   # наследуется метод .as_view()

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

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       # Добавляем в контекст объект фильтрации.
       context['filterset'] = self.filterset
       return context


class NewsDetail(DetailView):
   model = Post
   template_name = 'newsdetail.html'
   context_object_name = 'newsdetail'
