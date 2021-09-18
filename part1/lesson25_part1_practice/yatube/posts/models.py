from django.db import models


class Post(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    slug = models.SlugField(
        unique=True,
        max_length=200
    )
    text = models.TextField(
        help_text='Напишите текст',
        verbose_name='Текст',
    )
    pub_date = models.DateTimeField(
        "date published",
        auto_now_add=True
    )
    author = models.CharField(
        max_length=200,
        verbose_name='Автор',
        help_text='Укажите автора'
    )
    group = models.CharField(
        max_length=200,
        verbose_name='Группа',
        help_text='Дайте название группе'
    )

    def __str__(self):
        return self.text[:15]
