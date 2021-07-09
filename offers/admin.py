from django.contrib import admin

from .models import Offer


class OfferAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']
    class Meta:
        model = Offer

admin.site.register(Offer, OfferAdmin)