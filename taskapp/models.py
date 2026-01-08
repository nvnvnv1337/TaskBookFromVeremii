from django.db import models
from django.contrib.auth.models import User
class Task(models.Model):

    def __str__(self):
        return self.title

    title = models.CharField(max_length=30, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    completed = models.BooleanField(default=False, verbose_name='Выполнено')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Датта')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', related_name='tasks', blank=True)
