
# code
from django.db.models.signals import post_save, pre_delete, pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Product

from .utils import unique_slug_generator

# @receiver(pre_save, sender=Product)


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    print("Ici")
    if not instance.slug:
        instance.slug = "abc"
