from django.conf.urls import url
from django.urls import path,re_path

from .views import (
        OfferListView,
        OfferDetailSlugView,
        OfferFeaturedListView,
        )

urlpatterns = [
    path('', OfferListView.as_view(), name='list'),
    path('featured/', OfferFeaturedListView.as_view(), name='featured'),
    re_path('(?P<slug>[\w-]+)/$', OfferDetailSlugView.as_view(), name='detail'),
]