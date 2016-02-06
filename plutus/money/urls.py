from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^store_transactions/', views.store_transactions),
]