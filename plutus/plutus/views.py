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
import subprocess
import urllib

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
            percent = debits / (credits + debits)
        
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
        
        
def initiateChat(request):
    
    user = auth_sess(request.GET['sessionid'])

    if user.is_authenticated():
        response = subprocess.Popen("sh /home/ubuntu/workspace/plutus/plutus/chat1.sh", shell=True, stdout=subprocess.PIPE).stdout.read()
    
        response_dict = json.loads(response)
    
        dialog_id = response_dict['dialogs'][0]['dialog_id']
    
        dialog_id = str(dialog_id)
    
        x = "curl -X POST --header 'Content-Type: application/x-www-form-urlencoded' --header 'Accept: application/json' --header 'Authorization: Basic NjEwODhjNTQtY2E0Ny00N2Q2LWJkOWEtYjcyMGU1NzdhZTE2OjhFRDlyZFhiaXo4dg==' -d 'input=*' 'https://watson-api-explorer.mybluemix.net/dialog/api/v1/dialogs/74241df6-1e5f-4057-a838-143db2d45985/conversation'"


        results = subprocess.Popen(x, shell=True, stdout=subprocess.PIPE).stdout.read()     

        results = json.loads(results)

        conversation_id = results['conversation_id']
        client_id = results['client_id']
        
    
        #remove existing tokens for user
    
        modelz.ChatTokens.objects.all().filter(fk_to_user=user.id).delete()
        
        ct = modelz.ChatTokens()
        
        ct.fk_to_user = user
        ct.dialog_id = dialog_id
        ct.conversation_id = conversation_id
        ct.client_id = client_id
        ct.save()
        
        
        return HttpResponse(status=200)
        
def message(request):
    user = auth_sess(request.GET['sessionid'])

    if user.is_authenticated():
        
        tokenz = modelz.ChatTokens.objects.get(fk_to_user=user.id)
        
        dialog_id = tokenz.dialog_id
        conversation_id = tokenz.conversation_id
        client_id = tokenz.client_id
        
        
        message = request.GET['message']
        message = urllib.quote(message)
        
        x = "curl -X POST --header 'Content-Type: application/x-www-form-urlencoded' --header 'Accept: application/json' --header 'Authorization: Basic NjEwODhjNTQtY2E0Ny00N2Q2LWJkOWEtYjcyMGU1NzdhZTE2OjhFRDlyZFhiaXo4dg==' -d 'conversation_id="+conversation_id+"&client_id="+client_id+"&input="+message+"' 'https://watson-api-explorer.mybluemix.net/dialog/api/v1/dialogs/74241df6-1e5f-4057-a838-143db2d45985/conversation'"
        x = str(x)
        
        results = subprocess.Popen(x, shell=True, stdout=subprocess.PIPE).stdout.read()     
        
        results = json.loads(results)

        response = ""
        
        with fuckit: 
            response = results['response']

        return HttpResponse(response)