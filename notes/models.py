from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField("Наименование", max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Note(models.Model):
    category = models.ForeignKey(Category, models.PROTECT, related_query_name="category", related_name="category")
    name = models.CharField("Наименование", max_length=50)
    header = models.CharField("Заголовок", max_length=100)
    text = models.TextField("Текст заметки")
    password = models.CharField("Пароль", max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'заметка'
        verbose_name_plural = 'заметки'
        constraints = [
            models.UniqueConstraint(fields=['category', 'name'], name='unique_note')
        ]
