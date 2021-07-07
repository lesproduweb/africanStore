from django.urls import path,re_path

from .views import (
        AdListView,
        AdDetailSlugView,
        AdFeaturedListView,
        )

urlpatterns = [
    path('', AdListView.as_view(), name='list'),
    path('featured/', AdFeaturedListView.as_view(), name='featured'),
    re_path('(?P<slug>[\w-]+)/$', AdDetailSlugView.as_view(), name='detail'),
]