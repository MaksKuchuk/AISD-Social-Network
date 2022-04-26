"""xochu100pls URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path

import chat.views
import lc.views
import regauth.views
from xochu100pls import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', chat.views.index, name='chatpage'),
    path('lc/', lc.views.index, name='lcpage'),
    path('regauth/', regauth.views.index, name='regauthpage'),
    path('', (lambda x: redirect('regauth/', permanent=True))),

    path('regauth/ajax/signin/', regauth.views.signin, name='signin'),
    path('regauth/ajax/signup/', regauth.views.signup, name='signup'),

    path('lc/ajax/fillinfobylogin/', lc.views.fillinfobylogin, name='fillinfobylogin'),
    path('lc/ajax/updatelc/', lc.views.updatelc, name='updatelc'),
    path('lc/ajax/sendfriendrequest/', lc.views.sendfriendrequest, name='sendfriendrequest'),
    path('lc/ajax/getrequestlist/', lc.views.getrequestlist, name='getrequestlist'),
    path('lc/ajax/acceptfriend/', lc.views.acceptfriend, name='acceptfriend'),
    path('lc/ajax/denyfriend/', lc.views.denyfriend, name='denyfriend'),
    path('lc/ajax/getfriendlist/', lc.views.getfriendlist, name='getfriendlist'),

    path('chat/ajax/getmessages/', chat.views.getmessages, name='getmessages'),
    path('chat/ajax/update/', chat.views.update, name='update'),
    path('chat/ajax/addmessage/', chat.views.addmessage, name='addmessage'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
