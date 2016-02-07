from django.http import HttpResponse, JsonResponse
import json,re
import money.models as modelz
import goals.models as goalz
import datetime
import plutus.views as plutus
import goals.models as goalz
# from goals.models
from django.contrib.auth.models import User
from django.http import HttpResponse
import json
import models
import fuckit
from django.contrib.sessions.models import Session
from plutus.views import auth_sess

def auth(session_key):
    session = Session.objects.get(session_key=session_key)
    uid = session.get_decoded().get('_auth_user_id')
    user = User.objects.get(pk=uid)
    return user

def goalList(request):
    objs = modelz.MintTransaction.objects.all()

    respond = {}
    trans_fees = 0
    grocery_fees = 0
    coffe_shops = 0
    resturant = 0
    amazon_count = 0
    alcohol_count = 0
    yearly_income = 8000
    for x in objs:

        match_grow = re.search(r'Groceries',x.category)
        if match_grow:
            grocery_fees +=x.amount
        match_interest = re.search(r'Coffee Shops',x.category)
        if match_interest:
            coffe_shops +=x.amount

        match_resturant = re.search(r'Restaurants',x.category)
        if match_resturant:
            resturant += x.amount
        shopping_count = re.search(r'Shopping',x.category)
        if shopping_count:
            amazon_count += x.amount
        alcohol = re.search(r'Alcohol',x.category)
        if alcohol:
            alcohol_count += x.amount



    if (grocery_fees/yearly_income *100)>10:
        respond['Grocery'] = {}
        respond['Grocery']['statement'] = "Reduce Consumption below 10% you spend"
        respond['Grocery']['percent'] = 19
        respond['Grocery']['Number'] = str(grocery_fees/yearly_income*100)
    if (coffe_shops/yearly_income *100) > 0:
        respond['coffe_shops'] = {}
        respond['coffe_shops']['statement'] = "You spend a lot ,Meanwhile,Avg.CDN spend 30bucks"
        respond['coffe_shops']['percent'] = 0
        respond['coffe_shops']['Number'] = str(grocery_fees/yearly_income*100)

    if (resturant/yearly_income *100) >= 0:
       respond['resturant'] = {}
       respond['resturant']['statement'] = "Burn Calories, Save "
       respond['resturant']['percent'] = 0
       respond['coffe_shops']['Number'] = str(resturant/4)


    if (amazon_count/yearly_income *100) > 10:
        respond['amazon_count'] = {}
        respond['amazon_count']['statement'] = "Reduce and recyle.Your Shopping average: "
        respond['amazon_count']['percent'] = 12
        respond['coffe_shops']['Number'] = str(amazon_count/2)
    if (alcohol_count/yearly_income*100) > 2:
        respond['alcohol_count'] = {}
        respond['alcohol_count']['statement'] = "You may be a alcoholic. Avg"
        respond['amazon_count']['percent'] = 0
        respond['coffe_shops']['Number'] = str(alcohol_count/yearly_income)



    return HttpResponse(json.dumps(respond))
# from goals.models
def createGoal(request):
    
    
    return HttpResponse("Ok")
def view_levels(request):
    return JsonResponse(
  {
    "1": "0-50",
    "2": "50-100",
    "3": "150-300",
    "4": "300-500",
    "5": "500-750",
    "6": "750-1050",
    "7": "1050-1400",
    "8": "1400-1800",
    "9": "1800-2250",
    "10": "2250-2750",
    "11": "2750-3300",
    "12": "3300-3900"
  }
)
def giveme10(request):
    return JsonResponse({"1":"0"})