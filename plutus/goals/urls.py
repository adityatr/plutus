from django.conf.urls import url, include

from goals.views import view_levels
from goals.views import giveme10
urlpatterns = [
    url(r'^view_levels$', view_levels),
     url(r'^giveme10$', giveme10),
]
