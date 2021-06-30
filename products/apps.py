from django.apps import AppConfig
from django.db.models.signals import pre_save


class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'
    def ready(self):
        from .signals import product_pre_save_receiver
        pre_save.connect(product_pre_save_receiver, sender=self)
