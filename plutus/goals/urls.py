from django.conf.urls import url, include

from goals.views import view_levels,createGoal
from goals.views import giveme10,goalList
urlpatterns = [
    url(r'^view_levels$', view_levels),
    url(r'^giveme10$', giveme10),
    url(r'^createGoal$',createGoal),
    url(r'^goalList$',goalList)
]
