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
import re
from scipy.constants import year

import money.models as modelz
import datetime

# from goals.models
def recco(request):
    objs = modelz.MintTransaction.objects.all()

    respond = {}
    trans_fees = 0
    grocery_fees = 0
    match_interest_tagerine = 0
    resturant = 0
    amazon_count = 0
    check_tangerine_cc = 0
    for x in objs:
        match_fee = re.search(r'Fee',x.description)
        if match_fee:
           trans_fees  += x.amount
        match_grow = re.search(r'Groceries',x.category)
        if match_grow:
            grocery_fees +=x.amount
        match_interest = re.search(r'Interest',x.description)
        if match_interest:
            match_interest_tagerine +=x.amount

        match_resturant = re.search(r'Resturants',x.category)
        if match_resturant:
            resturant += x.amount
        shopping_count = re.search(r'Shopping',x.category)
        if shopping_count:
            amazon_count += x.amount

        tangerine_cc_checker = re.search(r'Tangerine Money-Back Credit Card',x.acc_name)
        if tangerine_cc_checker:
             check_tangerine_cc =1

    if trans_fees > 20:
        respond['EQ Bank'] = {}
        respond['EQ Bank']['statement'] = 'You overPaid in Fees,Get EQ Bank and save '
        respond['EQ Bank']['link'] = 'https://www.eqbank.ca/'
        respond['EQ Bank']['number'] = str(trans_fees)

    if grocery_fees/100 > 10:
        respond['Check Out 51'] = {}
        respond['Check Out 51']['statement'] = "Check Out 51 save around "
        respond['Check Out 51']['link'] = 'https://www.checkout51.com/'
        respond['Check Out 51']['number'] = str(grocery_fees/100)

    not_tangerine =  match_interest_tagerine - match_interest_tagerine/2
    if not_tangerine > 0:
        respond['tangerine'] = {}
        respond['tangerine']['statement'] = "Make Extra "+" Get a Tangerine Savings Account"
        respond['tangerine']['link'] = 'https://www.tangerine.ca/'
        respond['tangerine']['number'] = str(not_tangerine)


    if  check_tangerine_cc == 1:
        total_tag_saving = resturant +amazon_count +grocery_fees
        total_tag_saving = (2*total_tag_saving)/100 - (total_tag_saving)/100
        respond['tangerineCC'] = {}
        respond['tangerineCC']['statement'] = "You can save   with a Tangerine Credit Card"
        respond['tangerineCC']['link'] = 'https://www.tangerine.ca/'
        respond['tangerineCC']['number'] = str(total_tag_saving)
    return HttpResponse(json.dumps(respond))

def trend(request):
    return JsonResponse(
        {
            "creditCardPayment": "1000",
            "Housing": "700",
            "Entertaiment": "80",
            "Income": "3000",
            "Movies&DVD": "70",
            "Grocery": "450",
            "Saving":"400"
        }
    )