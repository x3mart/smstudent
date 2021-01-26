from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

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
    scientific = models.ForeignKey('ScientificArea', default=1, on_delete=models.PROTECT, verbose_name='Область науки')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


class PaperType(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тип работы'
        verbose_name_plural = 'Типы работ'

class Review(models.Model):
    body = models.TextField(verbose_name='Отзыв')
    rating = models.PositiveIntegerField(default=4, validators=[MinValueValidator(0), MaxValueValidator(5)], verbose_name='Оценка')
    release_date = models.DateField(auto_now_add=True, verbose_name='Опубликованно')
    student = models.OneToOneField('accounts.Student', blank=True, on_delete=models.PROTECT, parent_link=True, primary_key=True, verbose_name='Отзыв')

    # def __str__(self):
    #     return self.pk

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'