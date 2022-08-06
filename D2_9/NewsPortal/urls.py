from django.urls import path
# Импортируем созданные нами представления
from .views import NewsList, NewsDetail

urlpatterns = [
   # Django требует функцию, предоставляем ему метод класса as_view.
   # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
   # int — указывает на то, что принимаются только целочисленные значения
   path('<int:pk>', NewsDetail.as_view()),
   path('', NewsList.as_view()),
]