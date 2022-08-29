from django.urls import path
# Импортируем созданные нами представления
from .views import PostList, PostDetail, PostSearch, PostCreate, PostUpdate, PostDelete

urlpatterns = [
   # Django требует функцию, предоставляем ему метод класса as_view.
   # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
   # int — указывает на то, что принимаются только целочисленные значения
   path('<int:pk>/', PostDetail.as_view(), name='post_detail'), # name='post_detail' используется в reverse() model.py
   path('search/', PostSearch.as_view(), name='post_search'),  # D4.2 Не работает пока, на поиске нет ни поиска, ни пагинации
   path('create/', PostCreate.as_view(), name='post_create'),  #  D4.5
   path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),# D4.5
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),# D4.5
   path('', PostList.as_view()),
]

