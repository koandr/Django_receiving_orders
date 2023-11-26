from django.db import models
from django.utils import timezone

# Create your models here.


class Order(models.Model):
    order_dt = models.DateTimeField(default=timezone.now)
    order_name = models.CharField(max_length=200, verbose_name='Ім\'я')
    order_phone = models.CharField(max_length=200, verbose_name='Телефон')
    order_address = models.CharField(default='', max_length=200, verbose_name='Адреса')
    order_executor = models.CharField(default='', max_length=200, verbose_name='Виконувач')

    def __str__(self):
        return self.order_name
#        return self.order_address

    class Meta:
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'
