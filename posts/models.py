from django.conf import settings
from django.db import models
from django.utils.text import slugify

class Cats(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="Слаг")

    class Meta:
        ordering = ["name"]
        verbose_name = "Слаг"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    publish_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Автор",
                               related_name="posts")
    categoria = models.ManyToManyField(Cats, blank=True, verbose_name="Категория",
                                       related_name="post_category")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="слаг")

    class Meta:
        ordering = ['-publish_date']
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)



