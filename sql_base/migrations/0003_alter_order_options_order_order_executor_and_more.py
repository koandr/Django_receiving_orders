# Generated by Django 4.2.7 on 2023-11-25 21:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sql_base', '0002_alter_order_options_order_order_address_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Замовлення', 'verbose_name_plural': 'Замовлення'},
        ),
        migrations.AddField(
            model_name='order',
            name='order_executor',
            field=models.CharField(default='', max_length=200, verbose_name='Виконувач'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_dt',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
