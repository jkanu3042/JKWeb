from django.conf.urls import url, include
from django.contrib import admin

from .views import PostLV

urlpatterns = [
    url(r'^$', PostLV.as_view(), name='index'),
]
