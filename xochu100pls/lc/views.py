from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render

from lc.models import Lc, FriendRequestList, FriendList


def index(request):
    login = request.GET.get('login')

    per = Lc.objects.filter(login=login)[0]

    p = {
        'login': per.login,
        'name': per.name,
        'lastname': per.lastname,
        'photo': per.photo,
        'status': per.status,
        'education': per.education,
        'foodpreferences': per.foodpreferences,
        'attitudetoalcohol': per.attitudetoalcohol,
        'attitudetosmoking': per.attitudetosmoking,
    }

    return render(request, 'lc/index.html', p)

def fillinfobylogin(request):
    login = request.GET.get('login')

    per = Lc.objects.filter(login=login)[0]

    p = {
        'login': per.login,
        'name': per.name,
        'lastname': per.lastname,
        #'photo': per.photo,
        'status': per.status,
        'education': per.education,
        'foodpreferences': per.foodpreferences,
        'attitudetoalcohol': per.attitudetoalcohol,
        'attitudetosmoking': per.attitudetosmoking,
    }

    return JsonResponse(p)

def updatelc(request):
    login = request.GET.get('login')
    p = request.GET.get('p')
    val = request.GET.get('val')

    Lc.objects.filter(login=login).update(**{p: val})

    result = {}
    return JsonResponse(result)

def sendfriendrequest(request):
    loginfrom = request.GET.get('loginfrom')
    loginto = request.GET.get('loginto')

    if loginfrom == loginto:
        result = {'res': False}
        return JsonResponse(result)

    if len(Lc.objects.filter(login=loginto)) and len(FriendRequestList.objects.filter(loginfrom=loginfrom, loginto=loginto)) == 0 and len(FriendRequestList.objects.filter(loginfrom=loginto, loginto=loginfrom)) == 0:
        FriendRequestList(loginfrom=loginfrom, loginto=loginto).save()
        result = {'res': True}
    else:
        result = {'res': False}

    return JsonResponse(result)

def getrequestlist(request):
    login = request.GET.get('login')

    pers = FriendRequestList.objects.filter(loginto=login)
    p = {}

    for i in range(len(pers)):
        p[str(i)] = pers[i].loginfrom

    return JsonResponse(p)

def acceptfriend(request):
    login1 = request.GET.get('login1')
    login2 = request.GET.get('login2')

    FriendList(login1=login1, login2=login2).save()

    FriendRequestList.objects.filter(loginto=login1, loginfrom=login2).delete()
    FriendRequestList.objects.filter(loginto=login2, loginfrom=login1).delete()

    return JsonResponse({'i': 1})



def denyfriend(request):
    login1 = request.GET.get('login1')
    login2 = request.GET.get('login2')

    FriendRequestList.objects.filter(loginto=login1, loginfrom=login2).delete()
    FriendRequestList.objects.filter(loginto=login2, loginfrom=login1).delete()

    return JsonResponse({'i': 1})

def getfriendlist(request):
    login = request.GET.get('login')

    pers1 = FriendList.objects.filter(login1=login)
    pers2 = FriendList.objects.filter(login2=login)
    p = {}

    for i in range(len(pers1)):
        p[str(i)] = pers1[i].login2

    for i in range(len(pers2)):
        p[str(i + len(pers1))] = pers2[i].login1

    return JsonResponse(p)









