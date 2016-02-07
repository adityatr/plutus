from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^store_transactions$', views.store_transactions),
    url(r'^get_banks$', views.get_banks),
    url(r'^get_bills$', views.store_transactions),
    url(r'^get_categories$', views.get_categories),
    url(r'^set_budget$', views.save_budget),
    url(r'^get_budget$', views.get_budget),
]