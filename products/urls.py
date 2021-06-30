from django.conf.urls import url
from django.urls import path,re_path

from .views import (
        ProductListView,
        ProductDetailSlugView,
        ProductFeaturedListView,
        )

urlpatterns = [
    path('', ProductListView.as_view(), name='list_men'),
    path('featured/', ProductFeaturedListView.as_view(), name='featured_list'),
    re_path('(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='detail'),
]

