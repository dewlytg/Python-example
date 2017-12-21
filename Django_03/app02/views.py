from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
import json
from app02 import models
# Create your views here.

def business(request):
    v1 = models.Business.objects.all() # QuerySet对象列表
    v2 = models.Business.objects.all().values("id","capition") # 字典对象
    v3 = models.Business.objects.all().values_list("id","capition") # 元组对象
    return render(request,"business02.html",{"v1":v1,"v2":v2,"v3":v3})

def host(request):
    if request.method == "GET":
        v1 = models.Host.objects.filter (nid__gt=0).all ()
        v2 = models.Host.objects.filter (nid__gt=0).values ("nid", "hostname", "ip", "port", "b_id", "b__capition")
        v3 = models.Host.objects.filter (nid__gt=0).values_list ("nid", "hostname", "ip", "port", "b_id", "b__capition")
        b_list = models.Business.objects.all()
        return render(request, "host02.html", {"v1": v1, "v2": v2, "v3": v3, "b_list": b_list})
    elif request.method == "POST":
        h = request.POST.get("hostname",None)
        i = request.POST.get("ip",None)
        p = request.POST.get("port",None)
        b = request.POST.get("sel",None)
        models.Host.objects.create(hostname=h,ip=i,port=p,b_id=b)
        return redirect("/app02/host")

def add_ajax_host(request):
    try:
        ret = {"status": True, "error": None, "data": None}
        h = request.POST.get("hostname", None)
        i = request.POST.get("ip", None)
        p = request.POST.get("port", None)
        b = request.POST.get("sel", None)
        if h and len (h) > 5:
            models.Host.objects.create(hostname=h, ip=i, port=p, b_id=b)
        else:
            ret["status"] = False
            ret["error"] = "太短"
    except Exception as e:
        ret["status"] = False
        ret["error"] = "未知错误"
    finally:
        return HttpResponse(json.dumps(ret))

def edit_host(request):
    nid = request.POST.get("nid",None)
    h = request.POST.get("hostname",None)
    i = request.POST.get("ip",None)
    p = request.POST.get("port",None)
    b = request.POST.get("sel",None)
    models.Host.objects.filter(nid=nid).update(hostname=h,ip=i,port=p,b_id=b)
    return redirect("/app02/host")

def del_host(request):
    nid = request.POST.get("nid", None)
    models.Host.objects.filter(nid=nid).delete()
    return HttpResponse("删除成功")

def app(request):
    if request.method == "GET":
        app_list = models.Application.objects.all ()
        host_list = models.Host.objects.all ()
        return render (request, "app02.html", {"app_list": app_list, "host_list": host_list})
    elif request.method == "POST":
        appname = request.POST.get("appname",None)
        hlist = request.POST.getlist("hlist",None)
        obj = models.Application.objects.create(name=appname)
        obj.r.add(*hlist)
        obj.save()
        return redirect("/app02/app")

def add_ajax_app(request):
    try:
        ret = {"status": True, "error": None, "data": None}
        appname = request.POST.get("appname", None)
        hlist = request.POST.getlist("hlist", None)
        obj = models.Application.objects.create(name=appname)
        obj.r.add (*hlist)
        obj.save ()
    except Exception as e:
        ret["status"] = False
        ret["error"] = "应用组已经存在"
    finally:
        return HttpResponse(json.dumps(ret))

def edit_app(request):
    aid = request.POST.get("aid", None)
    appname = request.POST.get("appname", None)
    hlist = request.POST.getlist("hlist", None)
    obj = models.Application.objects.get(id=aid)
    obj.name = appname
    obj.r.set(hlist)
    obj.save()
    return redirect("/app02/app")

def del_app(request):
    aid = request.POST.get("aid",None)
    models.Application.objects.filter(id=aid).delete()
    return HttpResponse("Ok")