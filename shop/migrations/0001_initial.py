# Generated by Django 3.1.5 on 2021-01-26 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0004_auto_20210126_1842'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')),
                ('paid_at', models.DateTimeField(blank=True, verbose_name='Дата оплаты')),
                ('is_paid', models.BooleanField(default=False, verbose_name='Оплачено')),
                ('student', models.ManyToManyField(blank=True, to='accounts.Student', verbose_name='Покупатель')),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paper_title', models.CharField(max_length=255, verbose_name='Название работы')),
                ('paper_type', models.CharField(max_length=55, verbose_name='Тип работы')),
                ('paper_scientific', models.CharField(max_length=55, verbose_name='Область науки')),
                ('paper_subject', models.CharField(max_length=255, verbose_name='Предмет')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('author', models.ManyToManyField(blank=True, to='accounts.Author', verbose_name='Автор')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.order', verbose_name='Заказ')),
            ],
        ),
    ]
