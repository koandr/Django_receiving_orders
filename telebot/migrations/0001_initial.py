# Generated by Django 4.2.7 on 2023-11-14 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeleSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tg_token', models.CharField(max_length=200, verbose_name='Токен')),
                ('tg_chat', models.CharField(max_length=200, verbose_name='Чат айді')),
                ('tg_message', models.TextField(verbose_name='Текст сповіщення')),
            ],
            options={
                'verbose_name': 'Налаштування',
                'verbose_name_plural': 'Налаштування',
            },
        ),
    ]
