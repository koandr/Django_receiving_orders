from django.apps import AppConfig


class SqlBaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sql_base'
