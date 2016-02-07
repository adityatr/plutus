from django.conf.urls import url

from recco.views import recco,trend
from . import views

urlpatterns = [
    url(r'^promotion/$', recco),
    url(r'^communityTrend/$',trend)

]
