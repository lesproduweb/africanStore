from django.conf.urls import url
from django.urls import path, include, re_path


from .views import (
        SearchProductView,
        )

urlpatterns = [
    path('', SearchProductView.as_view(), name='query'),
]
