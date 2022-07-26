from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse


# Модель Author
# Модель, содержащая объекты всех авторов. Имеет следующие поля:
# связь «один к одному» с встроенной моделью пользователей User; (см. 2.6)
# рейтинг пользователя.
class Author(models.Model):
    author_user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)# verbose_name="Автор"
    rating = models.IntegerField(default=0)

    # Метод update_rating() модели Author, который обновляет рейтинг пользователя, переданный в аргумент этого метода.
    # Он состоит из следующего:
    # суммарный рейтинг каждой статьи автора умножается на 3;
    # суммарный рейтинг всех комментариев автора;
    # суммарный рейтинг всех комментариев к статьям автора.
    # Ниже будет дано описание того, как этот рейтинг можно посчитать.
    def update_rating(self):
        carma = 0

        # суммарный рейтинг каждой статьи автора умножается на 3;
        post_list = Post.objects.filter(author_user=self, type=Post.article)
        post_rating_list = post_list.values("rating")
        for item in post_rating_list:
            carma += 3 * item["rating"]

        # суммарный рейтинг всех комментариев автора;
        user = self.author_user
        comment_rating_list = Comment.objects.filter(author_user=user).values("rating")
        for item in comment_rating_list:
            carma += item["rating"]

        # суммарный рейтинг всех комментариев к статьям автора;
        for post in post_list:
            comment_in_post = Comment.objects.filter(post=post).values("rating")
            carma += sum(item["rating"] for item in comment_in_post)

        self.rating = carma
        self.save()

    def __str__(self):      # Не забываем добавлять,
        # Для читаемого имени автора на странице!
        # Для сравнения с {{ request.user }} тогда надо использовать {{ post_detail.post_author.author_user.username }}
        fullname = str(self.author_user.first_name) + ' ' + str(self.author_user.last_name)
        # Чтобы использовать более короткое {{ post_detail.post_author }} в сравнении с {{ request.user }}
        #username = str(self.author_user.username)
        return fullname


# Модель Category
# Категории новостей/статей — темы, которые они отражают (спорт, политика, образование и т. д.).
# Имеет единственное поле: название категории. Поле должно быть уникальным
# (в определении поля необходимо написать параметр unique = True).
class Category(models.Model):
    cat_name = models.CharField(max_length=20, unique=True)
#    subscribers = models.ManyToManyField(User) # Фигня получилась, нужно напрямую сделать связную таблицу

    def __str__(self):      # Не забываем добавлять, чтобы было читаемая категория при перечислении в формах!
        return self.cat_name #



# Модель Post
# Эта модель должна содержать в себе статьи и новости, которые создают пользователи.
# Каждый объект может иметь одну или несколько категорий.
# Соответственно, модель должна включать следующие поля:
# связь «один ко многим» с моделью Author;
# поле с выбором — «статья» или «новость»;
# автоматически добавляемая дата и время создания;
# связь «многие ко многим» с моделью Category (с дополнительной моделью PostCategory);
# заголовок статьи/новости;
# текст статьи/новости;
# рейтинг статьи/новости.


class Post(models.Model):
    # Кортеж POST_TYPE задаётся, чтобы иметь возможность брать человекочитаемое название из списка выбора
    # с помощью автоматически создаваемого метода get_FOO_display(), где FOO — это название поля.
    # Для варианта выбора (article, 'Статья') article = "AR" хранится в базе данных,
    # а название 'Статья' берётся через "AR" с помощью метода get_FOO_display() TODO D2.7
    article = "AR"
    news = "NS"
    POST_TYPE = [(article, 'Статья'), (news, 'Новость')]

    post_author = models.ForeignKey(Author, on_delete=models.PROTECT, verbose_name="Автор")
    type = models.CharField(max_length=2, choices=POST_TYPE, blank=False)#, default=article
    time_of_creation = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    category = models.ManyToManyField(Category, through="PostCategory", verbose_name="Категория")
    header = models.CharField(max_length=255, verbose_name="Название")  # TODO,
    text = models.TextField(verbose_name="Текст")  # TODO
    rating = models.IntegerField(default=0, verbose_name="Рейтинг")

    # Метод preview() модели Post, который возвращает начало статьи (предварительный просмотр) длиной 124 символа
    # и добавляет многоточие в конце.
    def preview(self):
        head = self.text[:124] + "..."
        return head

    # Методы like() и dislike() в моделях Comment и Post, которые увеличивают/уменьшают рейтинг на единицу.
    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def __str__(self):
        return self.header

    def get_absolute_url(self):
        # надо указать name='post_detail' в path() в urls.py
        #kwargs={'pk': self.pk})# str(self.type)+'/'+str(self.pk) # #
        absolute_url=reverse_lazy('post_detail', args=[str(self.pk)])
        return absolute_url


# Модель PostCategory
# Промежуточная модель для связи «многие ко многим» таблиц Post и Category:
# связь «один ко многим» с моделью Post;
# связь «один ко многим» с моделью Category.
class PostCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


#
# Модель Comment
# Под каждой новостью/статьёй можно оставлять комментарии, поэтому необходимо организовать их способ хранения тоже.
# Модель будет иметь следующие поля:
# связь «один ко многим» с моделью Post;
# связь «один ко многим» со встроенной моделью User
# (комментарии может оставить любой пользователь, необязательно автор);
# текст комментария;
# дата и время создания комментария;
# рейтинг комментария.
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    time_of_creation = models.DateTimeField(auto_now_add=True) # auto_now_add - автоустанавливает текущее время
    rating = models.IntegerField(default=0)

    # Методы like() и dislike() в моделях Comment и Post, которые увеличивают/уменьшают рейтинг на единицу.
    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
