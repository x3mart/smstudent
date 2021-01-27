from django.db import models


class Goods(models.Model):
    paper = models.ManyToManyField('paper.ReadyPaper', verbose_name='Покупатель')
    order = models.ForeignKey('Order', on_delete=models.CASCADE, verbose_name='Заказ')

class Order(models.Model):
    student = models.ManyToManyField('accounts.Student', blank=True, verbose_name='Покупатель')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения заказа')


class PaidOrder(models.Model):
    paper_title = models.CharField(max_length=255, verbose_name='Название работы')
    paper_type = models.CharField(max_length=55, verbose_name='Тип работы')
    paper_scientific = models.CharField(max_length=55, verbose_name='Область науки')
    paper_subject = models.CharField(max_length=255, verbose_name='Предмет')
    author = models.ManyToManyField('accounts.Author', blank=True, verbose_name='Автор')
    price = models.FloatField(verbose_name='Цена')