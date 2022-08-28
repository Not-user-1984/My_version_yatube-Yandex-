# Generated by Django 2.2.16 on 2022-08-19 14:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20220717_1320'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': 'Группу', 'verbose_name_plural': 'Группы'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-pub_date',), 'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
        migrations.AlterField(
            model_name='group',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='group',
            name='slug',
            field=models.SlugField(max_length=40, unique=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='group',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Название Группы'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='post',
            name='group',
            field=models.ForeignKey(blank=True, help_text='Группа к которой будет относиться пост ', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='groups', to='posts.Group', verbose_name='группа'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата Публикации'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(help_text='Текс поста', verbose_name='Текст поста'),
        ),
    ]
