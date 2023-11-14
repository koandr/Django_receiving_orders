from django.db import models

# Create your models here.

class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200, verbose_name='Ім\'я')
    order_phone = models.CharField(max_length=200, verbose_name='Телефон')
    order_address = models.CharField(default='', max_length=200, verbose_name='Адреса')

    def __str__(self):
        return self.order_name
#        return self.order_address

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Закази'
