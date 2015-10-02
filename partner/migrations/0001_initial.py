# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.CharField(max_length=20, verbose_name='Название', unique=True)),
                ('text', models.TextField(max_length=20000, verbose_name='Текст')),
            ],
        ),
        migrations.CreateModel(
            name='CarouselImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='carousel', verbose_name='Картинка')),
                ('text', models.CharField(blank=True, max_length=100, verbose_name='Подпись')),
                ('position', models.IntegerField(verbose_name='Позиция', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Наименование', unique=True)),
                ('description', models.TextField(max_length=5000, verbose_name='Описание')),
                ('manufacturer', models.CharField(max_length=60, verbose_name='Производитель')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
            ],
        ),
        migrations.CreateModel(
            name='EquipmentPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('price', models.IntegerField(blank=True, verbose_name='Цена')),
            ],
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение для вкладок')),
                ('header', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('text', models.TextField(max_length=10000, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=30, verbose_name='Отправитель')),
                ('email', models.EmailField(max_length=30, verbose_name='Email')),
                ('subject', models.CharField(max_length=50, verbose_name='Тема')),
                ('message', models.TextField(max_length=500, verbose_name='Сообщение')),
            ],
        ),
        migrations.CreateModel(
            name='MonitoringPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('price', models.IntegerField(blank=True, verbose_name='Цена')),
            ],
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=100, verbose_name='Контактный адресс')),
                ('email', models.EmailField(blank=True, max_length=50, verbose_name='Контактная почта')),
                ('phone1', models.CharField(blank=True, max_length=15, verbose_name='Телефон офиса')),
                ('phone2', models.CharField(blank=True, max_length=15, verbose_name='Телефон техподдержки')),
                ('latitude', models.CharField(max_length=10, verbose_name='Широта')),
                ('longitude', models.CharField(max_length=10, verbose_name='Долгота')),
                ('maptype', models.CharField(default='yandex#map', choices=[('yandex#map', 'Схема'), ('yandex#satellite', 'Спутник'), ('yandex#hybrid', 'Гибрид'), ('yandex#publicMap', 'Народная'), ('yandex#publicMapHybrid', 'Народная+Гибрид')], max_length=30, verbose_name='Тип карты')),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название', unique=True)),
                ('logo', models.ImageField(upload_to='', verbose_name='Логотип')),
                ('url', models.URLField(verbose_name='Ссылка на сайт')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('text', models.TextField(max_length=10000, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='SocialWidget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('vk', 'Вконтакте'), ('ok', 'Одноклассники'), ('fb', 'Facebook'), ('tw', 'Twitter'), ('li', 'LinkedIn'), ('yt', 'YouTube'), ('in', 'Instagram')], max_length=2, verbose_name='Название')),
                ('url', models.URLField(blank=True, verbose_name='Ссылка')),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('birth_day', models.DateField(verbose_name='День рождения')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('photo', models.ImageField(upload_to='', verbose_name='Фотография')),
                ('phone', models.CharField(max_length=100, verbose_name='Телефон')),
            ],
        ),
    ]
