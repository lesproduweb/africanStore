from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


# Create your models here.
from aStore.utils import upload_image_path

# from carts.models import Cart

# from addresses.models import Address

class GuestEmail(models.Model):
    email       = models.EmailField()
    active      = models.BooleanField(default=True)
    update      = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phoneNumber = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True, default="+216")
    # addresse =  models.ForeignKey(Address, on_delete=models.CASCADE)

    active      = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username