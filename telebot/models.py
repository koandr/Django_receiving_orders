from django.db import models

# Create your models here.

class TeleSetting(models.Model):
    tg_token = models.CharField(max_length=200, verbose_name='Токен')
    tg_chat = models.CharField(max_length=200, verbose_name='Чат айді')
    tg_message = models.TextField(verbose_name='Текст сповіщення')

    def __str__(self):
        return self.tg_chat

    class Meta:
        verbose_name = 'Налаштування'
        verbose_name_plural = 'Налаштування'
