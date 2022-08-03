from django.db import models
from django.contrib.auth.models import User


# Команды использования этой модели выполняются в консоли django и

# Модель Author
# Модель, содержащая объекты всех авторов. Имеет следующие поля:
# связь «один к одному» с встроенной моделью пользователей User; (см. 2.6)
# рейтинг пользователя.
class Author(models.Model):
    author_user = models.OneToOneField(User, on_delete=models.CASCADE)
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
        post_list = Post.objects.filter(id_author=self, type=Post.article)
        post_rating_list = post_list.values("rating")
        for item in post_rating_list:
            carma += 3 * item["rating"]

        # суммарный рейтинг всех комментариев автора;
        user = self.author_user
        comment_rating_list = Comment.objects.filter(id_user=user).values("rating")
        for item in comment_rating_list:
            carma += item["rating"]

        # суммарный рейтинг всех комментариев к статьям автора;
        for post in post_list:
            comment_in_post = Comment.objects.filter(id_post=post).values("rating")
            carma += sum(item["rating"] for item in comment_in_post)

        self.rating = carma
        self.save()


# Модель Category
# Категории новостей/статей — темы, которые они отражают (спорт, политика, образование и т. д.).
# Имеет единственное поле: название категории. Поле должно быть уникальным
# (в определении поля необходимо написать параметр unique = True).
class Category(models.Model):
    cat_name = models.CharField(max_length=20, unique=True)


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
    article = "AR"
    news = "NS"
    POST_TYPE = [(article, 'Статья'), (news, 'Новость')]

    post_author = models.ForeignKey(Author, on_delete=models.PROTECT)
    type = models.CharField(max_length=2, choices=POST_TYPE, default=article)
    time_of_creation = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through="PostCategory")
    header = models.CharField(max_length=255)  # TODO
    text = models.TextField()  # TODO
    rating = models.IntegerField(default=0)

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
    time_of_creation = models.DateTimeField(auto_created=True)
    rating = models.IntegerField(default=0)

    # Методы like() и dislike() в моделях Comment и Post, которые увеличивают/уменьшают рейтинг на единицу.
    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
