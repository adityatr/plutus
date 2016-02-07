from django.conf.urls import url
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
import urllib2
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
import json
import money.models as modelz
import fuckit
import datetime

def auth_sess(session_key):
    session = Session.objects.get(session_key=session_key)
    uid = session.get_decoded().get('_auth_user_id')
    user = User.objects.get(pk=uid)
    return user;



def auth(request):
    
    uname = request.GET['uname']
    pword = request.GET['pword']

    user = authenticate(username=uname, password=pword)

    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponse(request.session.session_key)
    else:
        return HttpResponse(status=503)
        
def whoami(request):
    return HttpResponse(request.user.username)
    
def progressbar2(request):

    if auth_sess(request.GET['sessionid']).is_authenticated():
        
        ret = {}
        ret['percent'] = "33";
        ret['expenditure'] = "5000.00"
        ret['income'] = "10000.00"
        
        return HttpResponse(json.dumps(ret));
        

def progressbar(request):
    
    user = auth_sess(request.GET['sessionid'])
    
    if user.is_authenticated():
        date = datetime.datetime
        year = date.today().year
        month = date.today().month
        objs = modelz.MintTransaction.objects.all().filter(fk_to_user=user.id,date__gt=datetime.date(year, month, 1))
        
        
        credits = 0
        debits = 0
        
        for x in objs:
            if x.acc_type == "credit":
                credits = credits + float(x.amount)
            elif x.acc_type == "debit":
                debits = debits + float(x.amount)
                
        percent = 0.5
        with fuckit:
            percent = credits / (credits + debits)
        
        ret = {}
        
        ret["income"] = str(credits)
        ret["expenditure"] = str(debits)
        ret["percent"] = str(percent * 100)
        
        if(month == 1):
            ret['month'] = "January"
        elif(month == 2):
            ret['month'] = "February"
        elif(month == 3):
            ret['month'] = "March"
        elif(month == 4):
            ret['month'] = "April"
        elif(month == 5):
            ret['month'] = "May"
        elif(month == 6):
            ret['month'] = "June"
        elif(month == 7):
            ret['month'] = "July"
        elif(month == 8):
            ret['month'] = "August"
        elif(month == 9):
            ret['month'] = "September"
        elif(month == 10):
            ret['month'] = "October"
        elif(month == 11):
            ret['month'] = "November"
        elif(month == 12):
            ret['month'] = "December"
        
        return HttpResponse(json.dumps(ret))