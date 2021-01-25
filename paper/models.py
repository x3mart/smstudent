from django.db import models
import random
import string
from django.utils.text import slugify
import unidecode
from unidecode import unidecode
import datetime


class Paper(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(max_length=240, unique=True, blank=True)
    description = models.TextField(verbose_name='Описание')
    pages = models.IntegerField( blank=True, null=True, verbose_name='Количество страниц')
    price = models.FloatField(default=0, verbose_name='Цена')
    path = models.FileField(blank=True, null=True, verbose_name='Файл')
    scientific = models.ForeignKey(
        'paper_attrs.ScientificArea',
        null=True,
        on_delete=models.PROTECT,
        verbose_name='Область науки',
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
        )
    subject = models.ForeignKey(
        'paper_attrs.Subject',
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        verbose_name='Предмет',
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
        )
    paper_type = models.ForeignKey(
        'paper_attrs.PaperType',
        null=True,
        on_delete=models.PROTECT,
        verbose_name='Тип работы',
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
        )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.title) + "-" + datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
        super(Paper, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class ReadyPaper(Paper):
    intro = models.TextField(verbose_name='Введение')
    content = models.TextField(verbose_name='Содержание')
    references = models.TextField(verbose_name='Список литературы')
    fragment = models.TextField(verbose_name='Отрывок')
    release_date = models.DateField(auto_now_add=True, verbose_name='Опубликованно')
    viewed = models.IntegerField(default=0, verbose_name='Просмотры')
    buyed = models.IntegerField(default=0, verbose_name='Куплена')
    originality = models.FloatField(default=0, verbose_name='Оригинальность')
    author = models.ForeignKey('accounts.Author', on_delete=models.PROTECT, verbose_name='Автор')


    class Meta:
        verbose_name = 'Готовая работа'
        verbose_name_plural = 'Готовые работы'
        ordering = ['-release_date']


class OrderedPaper(Paper):
    font_size = models.IntegerField(default=14, verbose_name='Размер шрифта')
    release_date = models.DateField( auto_now_add=True, verbose_name='Опубликованно')
    execution_date = models.DateField( blank=True, null=True, verbose_name='Дата сдачи заказа')
    status = models.ForeignKey('paper_attrs.OrderStatus', default=1, on_delete=models.PROTECT, verbose_name='Статус')
    author = models.ForeignKey('accounts.Author', on_delete=models.PROTECT, blank=True, null=True, verbose_name='Автор')
    student = models.ForeignKey('accounts.Student', on_delete=models.PROTECT, verbose_name='Заказчик')
    review = models.OneToOneField(
        'paper_attrs.Review',
        on_delete=models.PROTECT,
        related_name='ordered_paper',
        primary_key=True,
        parent_link=True,
        verbose_name='Отзыв'
        )
    class Meta:
        verbose_name = 'Заказ на работу'
        verbose_name_plural = 'Заказы на работу'