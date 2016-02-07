import user
from calendar import month

from django.http import HttpResponse, JsonResponse
from django.conf.urls import url
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
import urllib2
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
import json

from scipy.constants import year

import money.models as modelz
import datetime

# from goals.models
def recco(request):
    objs = modelz.MintTransaction.objects.all()
    return objs._fields
