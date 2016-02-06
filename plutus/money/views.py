from django.shortcuts import render
from django.http import HttpResponse
import json
import models
# Create your views here.
def store_transactions(request):
    
    if request.user.is_authenticated():
        if request.is_ajax():
            if request.method == 'POST':
                array = json.loads(request.body)
                
                for y in array:
                
                    x = models.Transaction()
                    x.primary_key = y['CONTAINER']
                    x.owner = request.user
                    x.basetype = y['basetype']
                    x.category = y['category']
                    x.description = y['description']
                    x.original_description = y['originalDescription']
                    x.date = y['date']
                    x.postDate = y['postDate']
                    x.merchantName = y['merchantName']
                    x.status = y['status']
                    x.accountID = y['accountID']
                    x.amount = y['amount']['amount']
                    x.currency_type = y['amount']['currency']
                    x.save()
        
                

    return HttpResponse(array)