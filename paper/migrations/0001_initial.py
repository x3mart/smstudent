# Generated by Django 3.1.5 on 2021-01-26 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_auto_20210126_1219'),
        ('paper_attrs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReadyPaper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('slug', models.SlugField(blank=True, max_length=240, unique=True)),
                ('description', models.TextField(verbose_name='Описание')),
                ('pages', models.IntegerField(blank=True, null=True, verbose_name='Количество страниц')),
                ('price', models.FloatField(default=0, verbose_name='Цена')),
                ('path', models.FileField(blank=True, null=True, upload_to='', verbose_name='Файл')),
                ('intro', models.TextField(verbose_name='Введение')),
                ('content', models.TextField(verbose_name='Содержание')),
                ('references', models.TextField(verbose_name='Список литературы')),
                ('fragment', models.TextField(verbose_name='Отрывок')),
                ('release_date', models.DateField(auto_now_add=True, verbose_name='Опубликованно')),
                ('viewed', models.IntegerField(default=0, verbose_name='Просмотры')),
                ('buyed', models.IntegerField(default=0, verbose_name='Куплена')),
                ('originality', models.FloatField(default=0, verbose_name='Оригинальность')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.author', verbose_name='Автор')),
                ('paper_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='paper_readypaper_related', related_query_name='paper_readypapers', to='paper_attrs.papertype', verbose_name='Тип работы')),
                ('scientific', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='paper_readypaper_related', related_query_name='paper_readypapers', to='paper_attrs.scientificarea', verbose_name='Область науки')),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='paper_readypaper_related', related_query_name='paper_readypapers', to='paper_attrs.subject', verbose_name='Предмет')),
            ],
            options={
                'verbose_name': 'Готовая работа',
                'verbose_name_plural': 'Готовые работы',
                'ordering': ['-release_date'],
            },
        ),
        migrations.CreateModel(
            name='OrderedPaper',
            fields=[
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('slug', models.SlugField(blank=True, max_length=240, unique=True)),
                ('description', models.TextField(verbose_name='Описание')),
                ('pages', models.IntegerField(blank=True, null=True, verbose_name='Количество страниц')),
                ('price', models.FloatField(default=0, verbose_name='Цена')),
                ('path', models.FileField(blank=True, null=True, upload_to='', verbose_name='Файл')),
                ('font_size', models.IntegerField(default=14, verbose_name='Размер шрифта')),
                ('release_date', models.DateField(auto_now_add=True, verbose_name='Опубликованно')),
                ('execution_date', models.DateField(blank=True, null=True, verbose_name='Дата сдачи заказа')),
                ('review', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, parent_link=True, primary_key=True, related_name='ordered_paper', serialize=False, to='paper_attrs.review', verbose_name='Отзыв')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.author', verbose_name='Автор')),
                ('paper_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='paper_orderedpaper_related', related_query_name='paper_orderedpapers', to='paper_attrs.papertype', verbose_name='Тип работы')),
                ('scientific', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='paper_orderedpaper_related', related_query_name='paper_orderedpapers', to='paper_attrs.scientificarea', verbose_name='Область науки')),
                ('status', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='paper_attrs.orderstatus', verbose_name='Статус')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.student', verbose_name='Заказчик')),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='paper_orderedpaper_related', related_query_name='paper_orderedpapers', to='paper_attrs.subject', verbose_name='Предмет')),
            ],
            options={
                'verbose_name': 'Заказ на работу',
                'verbose_name_plural': 'Заказы на работу',
            },
        ),
    ]
