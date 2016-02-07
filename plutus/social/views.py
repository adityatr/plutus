from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from . import models
import json
# Create your views here.

def getUsers(request):
    
    x = User.objects.all()
    
    ret = {}
    count = 0
    for usr in x:
        
        ret[count] = {}
        
        pts = 0
        try:
            pts = models.Achievments.objects.get(primary_key=usr.id).points
        except Exception:
            ret[count]['score'] = pts 
            ret[count]['name'] = usr.username        
            
        ret[count]['score'] = pts 
        ret[count]['name'] = usr.username
        count = count + 1;
    
    return HttpResponse(json.dumps(ret))
        
