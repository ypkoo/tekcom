from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from .views import index

urlpatterns = [
    url('new', index, name='index'),
]