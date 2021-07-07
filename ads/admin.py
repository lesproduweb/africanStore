from django.contrib import admin

from .models import Ad


class AdAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']
    class Meta:
        model = Ad

admin.site.register(Ad, AdAdmin)