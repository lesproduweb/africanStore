from django.conf.urls import url
from django.urls import path,re_path

from .views import (
        FreeProductListView,
        FreeProductDetailSlugView,
        FreeProductFeaturedListView,
        )

urlpatterns = [
    path('', FreeProductListView.as_view(), name='list'),
    path('featured/', FreeProductFeaturedListView.as_view(), name='featured'),
    re_path('(?P<slug>[\w-]+)/$', FreeProductDetailSlugView.as_view(), name='detail'),
]