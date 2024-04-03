from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


# do not work
class Tags(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"


class UsersEmail(models.Model):
    user_email = models.CharField(max_length=255)

    def __str__(self):
        return self.user_email

    class Meta:
        verbose_name = "Користувачі для розсилки"
        verbose_name_plural = "Користувачі для розсилки"


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=30, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Опис")
    published_date = models.DateTimeField(auto_created=True, verbose_name="Дата")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категорія")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    image = models.URLField(default="http://placehold.it/900x300")
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Пости"


class Comments(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE, verbose_name="Назва посту")
    username = models.CharField(max_length=30, verbose_name="Username")
    body = models.CharField(max_length=500, verbose_name="Comment")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата")

    def __str__(self):
        return f'Comment by {self.username} on {self.post}'
        pass

    class Meta:
        verbose_name = "Коментар"
        verbose_name_plural = "Коментари"

