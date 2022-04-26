from django.shortcuts import render
from django.db.models import Q
from django.http import JsonResponse

from chat.models import Chat
from lc.models import FriendList, Lc


def index(request):
    login = request.GET.get('login')
    name = request.GET.get('name')

    return render(request, 'chat/index.html', {'login': login, 'name': name})

def getmessages(request):
    loginfrom = request.GET.get('loginfrom')
    loginto = request.GET.get('loginto')

    msg = Chat.objects.filter(Q(loginfrom=loginfrom, loginto=loginto) | Q(loginfrom=loginto, loginto=loginfrom))

    msgs = {}
    for i in range(len(msg)):
        if msg[i].loginfrom == loginfrom:
            msgs[str(i)] = '<myyyyyyy..>' + msg[i].message
        else:
            msgs[str(i)] = '<notmyyyy..>' + msg[i].message

    return JsonResponse(msgs)

def update(request):
    login = request.GET.get('login')

    fr = FriendList.objects.filter(Q(login1=login) | Q(login2=login))
    p = {}

    for i in range(len(fr)):
        if fr[i].login1 == login:
            p[str(i)] = fr[i].login2
            p[str(i) + 'name'] = Lc.objects.filter(login=fr[i].login2)[0].name
        else:
            p[str(i)] = fr[i].login1
            p[str(i) + 'name'] = Lc.objects.filter(login=fr[i].login1)[0].name

    p['size'] = len(fr)

    return JsonResponse(p)

def addmessage(request):
    loginfrom = request.GET.get('loginfrom')
    loginto = request.GET.get('loginto')
    message = request.GET.get('message')

    Chat(loginfrom=loginfrom, loginto=loginto, message=message).save()

    return JsonResponse({'is': True})


