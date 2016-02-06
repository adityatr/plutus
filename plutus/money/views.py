from django.shortcuts import render
from django.http import HttpResponse
import json
import models
import fuckit

# Create your views here.
def store_transactions(request):
    
    if request.user.is_authenticated():
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

    if request.user.is_authenticated():

            b = models.BankAccount.objects.all().filter(primary_key=request.user.id)
            
            ret = {}
            
            for x in b:
                
                ret["bank" + str(x.id)] = {}
                
                ret["bank" + str(x.id)]['title'] = x.title
                ret["bank" + str(x.id)]['balance'] = str(x.balance)
                ret["bank" + str(x.id)]['credit'] = str(x.credit)
                ret["bank" + str(x.id)]['debit'] = str(x.debit)
            return HttpResponse(json.dumps(ret))
    return HttpResponse(status=500)
    
            
            