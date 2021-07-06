"""aStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth.views import LogoutView

# from products.views import ProductListView, ProductDetailView, detail
from .views import home_page, contact_page
from accounts.views import login_page, register_page, guest_register_view


urlpatterns = [
    path('', home_page, name='home'),
    path('admin/', admin.site.urls, name='login'),
    path('login/', login_page, name='login'),
    # path('logout/', logout_view, name='logout'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register_page, name='register'),
    path('register/guest', guest_register_view, name='guest_register'),
    path('contact/', contact_page, name='contact'),
    path('products/', include(('products.urls', 'products'), namespace='products')),
    path('search/', include(('search.urls', 'search'), namespace='search')),
    path('carts/', include(('carts.urls', 'carts'), namespace='cart')),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
