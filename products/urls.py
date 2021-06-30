from django.conf.urls import url

from .views import (
        ProductListView,
        ProductDetailSlugView,
        ProductFeaturedListView,
        )

urlpatterns = [
    url(r'^products/men', ProductListView.as_view(), name='list_men'),
    url(r'^products/featured/$', ProductFeaturedListView.as_view(), name='featured_list'),
    url(r'products/(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='detail'),
]

