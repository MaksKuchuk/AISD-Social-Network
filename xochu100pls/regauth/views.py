from django.http import JsonResponse
from django.shortcuts import render

from lc.models import Lc
from regauth.models import Regauth


def index(request):
    return render(request, 'regauth/index.html')

def signin(request):
    login = request.GET.get('login')
    password = request.GET.get('pass')

    pers = Regauth.objects.filter(login=login, password=password)
    if len(pers):
        result = {'is': True, 'login': pers[0].login}
    else:
        result = {'is': False}

    return JsonResponse(result)

def signup(request):
    login = request.GET.get('login')
    password = request.GET.get('pass')

    if not len(Regauth.objects.filter(login=login)):
        result = {'is': True}
        Lc(login=login, name='unnamed').save()
        Regauth(login=login, password=password).save()
    else:
        result = {'is': False}

    return JsonResponse(result)


