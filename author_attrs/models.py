from django.db import models

    
class LearningPhase(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Стадия обучения'
        verbose_name_plural = 'Стадии обучения'


class AcademicTitle(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Научное звание'
        verbose_name_plural = 'Научные звания'


class ScientificRank(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ученая степень'
        verbose_name_plural = 'Ученая степень'


class Portfolio(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    path = models.FileField(blank=True, verbose_name='Файл')