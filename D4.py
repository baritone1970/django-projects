#2) Добавьте страницу /news/search. На ней должна быть реализована возможность искать новости
#   по определённым критериям. Критерии должны быть следующие:
#   * по названию;
#   * по категории;
#   * позже указываемой даты.

#3) Запрограммировать страницы создания, редактирования и удаления новостей и статей.
#   Страницы рекомендуется расположить по следующим ссылкам:
#   - /news/create/
#   - /news/<int:pk>/edit/
#   - /news/<int:pk>/delete/
#   - /articles/create/
#   - /articles/<int:pk>/edit/
#   - /articles/<int:pk>/delete/

# Идея: выводить это должна одна и та же страница, просто там должна быть фильтрация по скрытому параметру:
# статья или новость.

# Проверка формы:
#  python manage.py shell
#>>> from NewsPortal.forms import PostForm
#>>> f = PostForm({'category': [8], 'header': 'sjfdsjkfdlkzjcv', 'text': 'slfddsz_fcjmzslrfmsr'})
#>>> f = PostForm({'post_author': 3, 'category': [8], 'header': 'sjfdsjkfdlkzjcv', 'text': 'slfddsz_fcjmzslrfmsr'})
#>>> f.is_valid()
#>>> f.errors
#>>> print(f)

#TODO ПРи создании поста через форму ошибка ввода пользователя. запрограммируем аутентификацию сначала.