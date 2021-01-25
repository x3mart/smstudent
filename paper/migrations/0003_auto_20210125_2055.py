# Generated by Django 3.1.5 on 2021-01-25 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0002_auto_20210125_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderedpaper',
            name='path',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='orderedpaper',
            name='release_date',
            field=models.DateField(auto_now_add=True, verbose_name='Опубликованно'),
        ),
        migrations.AlterField(
            model_name='readypaper',
            name='path',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Файл'),
        ),
    ]
