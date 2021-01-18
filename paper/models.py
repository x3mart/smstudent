from django.db import models

class OrderStatus(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статус закза'
        verbose_name_plural = 'Статусы заказа'


class ScientificArea(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Область науки'
        verbose_name_plural = 'Области науки'


class Subject(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    status = models.ForeignKey('ScientificArea', default=1, on_delete=models.PROTECT, verbose_name='Область науки')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


class Paper(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    title_slug = models.SlugField(max_length=240)
    description = models.TextField(verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена')
    path = models.FileField(blank=True, verbose_name='Файл')
    scientific = models.ForeignKey('ScientificArea', null=True, on_delete=models.PROTECT, verbose_name='Область науки')
    subject = models.ForeignKey('Subject', null=True, on_delete=models.PROTECT, verbose_name='Предмет')

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class ReadyPaper(Paper):
    intro = models.TextField(verbose_name='Введение')
    content = models.TextField(verbose_name='Содержание')
    references = models.TextField(verbose_name='Список литературы')
    fragment = models.TextField(verbose_name='Отрывок')
    pages = models.IntegerField(verbose_name='Количество страниц')
    release_date = models.DateField(auto_now_add=True, verbose_name='Опубликованно')
    viewed = models.IntegerField(default=0, verbose_name='Просмотры')
    buyed = models.IntegerField(default=0, verbose_name='Куплена')
    originality = models.FloatField(default=0, verbose_name='Оригинальность')


    class Meta:
        verbose_name = 'Готовая работа'
        verbose_name_plural = 'Готовые работы'
        ordering = ['-release_date']

class OrderedPaper(Paper):
    wishes = models.CharField(blank=True, max_length=200, verbose_name='Пожелания')
    status = models.ForeignKey('OrderStatus', default=1, on_delete=models.PROTECT, verbose_name='Статус')

    class Meta:
        verbose_name = 'Заказ на работу'
        verbose_name_plural = 'Заказы на работу'
