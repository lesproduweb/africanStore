from django.conf.urls import url
from django.urls import path, include, re_path


from .views import (
        SearchView,
        )

urlpatterns = [
    path('', SearchView.as_view(), name='query'),
]
