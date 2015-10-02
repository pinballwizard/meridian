# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, verbose_name='Название', max_length=50)),
                ('pub_date', models.DateField(verbose_name='Время публикации')),
                ('text', ckeditor.fields.RichTextField(verbose_name='Текст', max_length=20000)),
            ],
            options={
                'verbose_name_plural': 'Новости',
                'verbose_name': 'Новость',
            },
        ),
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sender', models.CharField(verbose_name='Отправитель', max_length=30)),
                ('email', models.EmailField(verbose_name='Email', max_length=30)),
                ('subject', models.CharField(verbose_name='Тема', max_length=50)),
                ('message', models.TextField(verbose_name='Сообщение', max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Письма',
                'verbose_name': 'Письмо',
            },
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Название компании', max_length=100)),
                ('address', models.CharField(verbose_name='Контактный адресс', max_length=100)),
                ('email', models.EmailField(blank=True, verbose_name='Контактная почта', max_length=50)),
                ('phone1', models.CharField(blank=True, verbose_name='Телефон Офис', max_length=15)),
                ('phone2', models.CharField(blank=True, verbose_name='Телефон Тех.поддержки', max_length=15)),
                ('description', models.TextField(blank=True, verbose_name='Метаописание сайта', max_length=200)),
                ('keywords', models.TextField(blank=True, verbose_name='Ключевые слова для поиска', max_length=200)),
                ('latitude', models.CharField(verbose_name='Широта', max_length=10)),
                ('longitude', models.CharField(verbose_name='Долгота', max_length=10)),
                ('maptype', models.CharField(default='yandex#map', max_length=30, verbose_name='Тип карты', choices=[('yandex#map', 'Схема'), ('yandex#satellite', 'Спутник'), ('yandex#hybrid', 'Гибрид'), ('yandex#publicMap', 'Народная'), ('yandex#publicMapHybrid', 'Народная+Гибрид')])),
            ],
            options={
                'verbose_name_plural': 'Офис',
                'verbose_name': 'Офисы',
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, verbose_name='Название', max_length=20)),
                ('logo', models.ImageField(upload_to='partner', verbose_name='Логотип')),
                ('url', models.URLField(verbose_name='Ссылка на сайт')),
            ],
            options={
                'verbose_name_plural': 'Партнеры',
                'verbose_name': 'Партнер',
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Название', max_length=30)),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('sale', models.BooleanField(verbose_name='Акция', help_text='Указать отображение на главной странице')),
            ],
            options={
                'verbose_name_plural': 'Цены',
                'verbose_name': 'Цена',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Название проекта', max_length=100)),
                ('face_image', models.ImageField(upload_to='project', verbose_name='Заставка')),
            ],
            options={
                'verbose_name_plural': 'Проекты',
                'verbose_name': 'Проект',
            },
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to='project', verbose_name='Картинка')),
                ('text', models.CharField(blank=True, verbose_name='Комментарий', max_length=500)),
                ('project', models.ForeignKey(to='santech.Project')),
            ],
            options={
                'verbose_name_plural': 'Фотографии проекта',
                'verbose_name': 'Фотография проекта',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('owner', models.CharField(unique=True, verbose_name='Клиент', max_length=50)),
                ('header', models.CharField(verbose_name='Заголовок', max_length=20)),
                ('text', models.CharField(verbose_name='Отзыв', max_length=500)),
                ('grade', models.IntegerField(default=5, verbose_name='Оценка', choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
            ],
            options={
                'verbose_name_plural': 'Отзывы',
                'verbose_name': 'Отзыв',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to='service', verbose_name='Изображение')),
                ('header', models.CharField(unique=True, verbose_name='Заголовок', max_length=20)),
                ('text', ckeditor.fields.RichTextField(blank=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name_plural': 'Услуги',
                'verbose_name': 'Услуга',
            },
        ),
        migrations.CreateModel(
            name='SocialWidget',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=2, verbose_name='Название', choices=[('vk', 'Вконтакте'), ('ok', 'Одноклассники'), ('fb', 'Facebook'), ('tw', 'Twitter'), ('li', 'LinkedIn'), ('yt', 'YouTube'), ('in', 'Instagram')])),
                ('url', models.URLField(blank=True, verbose_name='Ссылка')),
                ('office', models.ForeignKey(to='santech.Office')),
            ],
            options={
                'verbose_name_plural': 'Социальные виджеты',
                'verbose_name': 'Социальный виджет',
            },
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Имя', max_length=30)),
                ('last_name', models.CharField(verbose_name='Фамилия', max_length=30)),
                ('birth_day', models.DateField(verbose_name='День рождения')),
                ('email', models.EmailField(verbose_name='Почта', max_length=254)),
                ('photo', models.ImageField(upload_to='worker', verbose_name='Фотография')),
                ('phone', models.CharField(verbose_name='Телефон', max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Работники',
                'verbose_name': 'Работник',
            },
        ),
    ]
