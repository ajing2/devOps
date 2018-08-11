from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from salt.forms import SystemInit
from salt.models import AppList
# from util.masterApp import publicKey
from util.saltapi import SaltServer


def index(request):
    return HttpResponse("hello salt")

def installApp(request):
    return render(request, 'installapp.html')

def applist(request):
    resultBean = dict()
    appList = AppList.objects.all()
    if appList:
        try:
            appAll = list()
            for item in appList:
                each = dict()
                each['id'] = item.id
                each['priority'] = item.priority
                each['appname'] = item.appname
                appAll.append(each)
            resultBean['code'] = 200
            resultBean['msg'] = 'success'
            resultBean['data'] = appAll
        except Exception as e:
            resultBean['code'] = 400
            resultBean['msg'] = 'error'
            resultBean['data'] = None
        return  JsonResponse(resultBean)
    else:
        resultBean['code'] = 400
        resultBean['msg'] = 'error'
        resultBean['data'] = None

@login_required
def init(request):
    if request.method == "GET":
        return render(request, 'init.html')
    elif request.method == "POST":
        iptext = request.POST.get("iptext")
        checkbox = request.POST.getlist("Checkbox")
        saltServer = SaltServer()
        initDict = {
            '1': "publicKey",
            '2': "installMinionid"
        }
        if len(checkbox)>0:
            for i in checkbox:
                if i in initDict.keys():
                    for ip in iptext.split(","):
                        if ip.strip():
                            result1 = saltServer.runRunner('masterApp.' + initDict.get(i), ipaddr=ip.strip())
                            print(result1)

        return HttpResponse("success")