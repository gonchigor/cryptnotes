# Generated by Django 2.2.5 on 2019-09-02 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Наименование'),
        ),
    ]
