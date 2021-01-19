# Generated by Django 3.1.5 on 2021-01-19 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0003_auto_20210119_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderedpaper',
            name='slug',
            field=models.SlugField(blank=True, max_length=240, unique=True),
        ),
        migrations.AlterField(
            model_name='orderedpaper',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='paper.subject', verbose_name='Предмет'),
        ),
        migrations.AlterField(
            model_name='readypaper',
            name='slug',
            field=models.SlugField(blank=True, max_length=240, unique=True),
        ),
        migrations.AlterField(
            model_name='readypaper',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='paper.subject', verbose_name='Предмет'),
        ),
    ]
