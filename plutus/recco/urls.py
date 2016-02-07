from django.conf.urls import url

from recco.views import recco
from . import views

urlpatterns = [
    url(r'^recco/$', recco),
    
]
