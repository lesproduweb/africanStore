from django.conf.urls import url
from django.urls import path
from .views import (
        cart_home,
        cart_update,
        checkout,
        )

urlpatterns = [
    path('', cart_home, name='home'),
    path('update/', cart_update, name='update'),
    path('checkout/', checkout, name='checkout'),
]
