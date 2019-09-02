from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField("Наименование", max_length=50, unique=True)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

