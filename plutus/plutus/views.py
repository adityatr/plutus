from django.conf.urls import url
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

def auth(request):
    
    uname = request.GET['uname']
    pword = request.GET['pword']

    user = authenticate(username=uname, password=pword)

    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponse("1")
    else:
        return HttpResponse("0")