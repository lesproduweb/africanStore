from django.contrib import admin

# Register your models here.
from .models import GuestEmail
from .models import Account

admin.site.register(Account)

admin.site.register(GuestEmail)