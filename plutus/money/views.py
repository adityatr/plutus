from django.shortcuts import render
from django.http import HttpResponse
import json
import models
import fuckit
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User

# Create your views here.
def auth(session_key):
    session = Session.objects.get(session_key=session_key)
    uid = session.get_decoded().get('_auth_user_id')
    user = User.objects.get(pk=uid)
    return user;


def store_transactions(request):
    
    if auth(request.GET['sessionid']).is_authenticated():
        if request.method == 'POST':
            array = json.loads(request.body)['transaction']
                    
            for y in array:
    
                            
                x = models.Transaction()
                with fuckit:
                    x.primary_key = y['id']
                with fuckit:
                    x.CONTAINER = y['CONTAINER']
                with fuckit:
                    x.owner = request.user
                with fuckit:
                    x.basetype = y['baseType']
                with fuckit:
                    x.category = y['category']
                with fuckit:    
                    x.description = y['description']
                with fuckit:
                    x.original_description = y['originalDescription']
                with fuckit:
                    x.date = y['date']
                with fuckit:
                    x.postDate = y['postDate']
                with fuckit:
                    x.merchantName = y['merchantName']
                with fuckit:
                    x.status = y['status']
                with fuckit:
                    x.accountID = y['accountId']
                with fuckit:
                    x.amount = y['amount']['amount']
                with fuckit:
                    x.currency_type = y['amount']['currency']
                x.save()
                    
            return HttpResponse("done")

def get_banks(request):
    
    user =auth(request.GET['sessionid']);

    if user.is_authenticated():

            b = models.BankAccount.objects.all().filter(primary_key=user.id)
            
            ret = {}
            
            for x in b:
                
                ret["bank" + str(x.id)] = {}
                
                ret["bank" + str(x.id)]['title'] = x.title
                ret["bank" + str(x.id)]['balance'] = str(x.balance)
                ret["bank" + str(x.id)]['credit'] = str(x.credit)
                ret["bank" + str(x.id)]['debit'] = str(x.debit)
                
            return HttpResponse(json.dumps(ret))
    else:
        return HttpResponse(status=503)
    

def get_categories(request):
    user =auth(request.GET['sessionid']);

    if user.is_authenticated():
        ret = {}
        
        objs = models.MintTransaction.objects.all()
        
        for x in objs: 
            
            if str(x.category) in ret.keys():
                ret[str(x.category)] = str(float(ret[str(x.category)]) + float(x.amount))
            else:
                ret[str(x.category)] = str(x.amount)
            
            
    return HttpResponse(json.dumps(ret))
    
def get_budget(request):
    
    user =auth(request.GET['sessionid']);
    
    budget = models.Budget.objects.all().get(fk_to_user=user.id)
    

    return HttpResponse(budget.budget);
    
    
def save_budget(request):
    
    user =auth(request.GET['sessionid']);
    
    models.Budget.objects.all().filter(fk_to_user=user.id).delete()
    
    budget = models.Budget()
    
    
    budget.fk_to_user = user
    budget.budget = request.GET['budget']
    budget.save()
    
    
    return HttpResponse(status=200);