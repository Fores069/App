from django.db import models


class Task(models.Model):
    """Задачи"""
    title = models.CharField('Заголовок',max_length=50)
    description = models.TextField('Описание')

    def __str__(self):
        return f'{self.title} {self.description}'

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

    def get_absolute_url(self):
        return '/'