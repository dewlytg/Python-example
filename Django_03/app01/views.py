from django.shortcuts import render,redirect,HttpResponse
from app01 import models
import json
# Create your views here.

def business(request):
    # QuerySet 类型
    # [obj(id,caption,code),obj(id,caption,code),obj(id,caption,code)]
    v1 = models.Business.objects.all()

    # QuerySet 类型
    # [{"id":1,"caption":运维},{"id":2,"caption":市场}]
    v2 = models.Business.objects.all().values("id","caption")

    # QuerySet 类型
    # [(1,"运维"),(2,"市场")]
    v3 = models.Business.objects.all().values_list("id","caption")

    return render(request,"business.html",{"v1":v1,"v2":v2,"v3":v3})

# def host(request):
#     v1 = models.Host.objects.filter(nid__gt=0)
#     # for obj in v1:
#     #     print(obj.nid,obj.hostname,obj.ip,obj.port)
#     #     print(obj.b,obj.b_id,obj.b.id,obj.b.caption,obj.b.code)
#
#     # 只有models中的obj对象调用的使用可以用".",obj.b.id obj.b.caption
#     # 如果是在查询条件中因为使用的字符串查询,不是一个对象,必须要使用"__"来代替"."
#     v2 = models.Host.objects.filter(nid__gt=0).values("nid","hostname","port","b_id","b__caption")
#     # for row in v2:
#     #     print(row)
#
#     v3 = models.Host.objects.filter(nid__gt=0).values_list("nid","hostname","port","b_id","b__caption")
#
#     return render(request,"host.html",{"v1":v1,"v2":v2,"v3":v3})

def host(request):
    if request.method == "GET":
        v1 = models.Host.objects.filter (nid__gt=0)
        v2 = models.Host.objects.filter (nid__gt=0).values ("nid", "hostname", "port", "b_id", "b__caption")
        v3 = models.Host.objects.filter (nid__gt=0).values_list ("nid", "hostname", "port", "b_id", "b__caption")
        caption_list = models.Business.objects.all()
        print(caption_list)
        return render(request,"host.html",{"v1":v1,"v2":v2,"v3":v3,"caption_list":caption_list})
    elif request.method == "POST":
        h = request.POST.get("hostname",None)
        i = request.POST.get("ip",None)
        p = request.POST.get("port",None)
        b_id = request.POST.get("b_id",None)
        models.Host.objects.create(
            hostname=h,
            ip = i,
            port = p,
            b_id = b_id
        )
        return redirect("/host")

def test_ajax(request):
    ret = {"status":True,"error":None,"data":None}
    try:
        h = request.POST.get ("hostname", None)
        i = request.POST.get ("ip", None)
        p = request.POST.get ("port", None)
        b_id = request.POST.get ("b_id", None)
        if h and len (h) > 5:
            models.Host.objects.create (
                hostname=h,
                ip=i,
                port=p,
                b_id=b_id
            )
        else:
            ret["status"] = False
            ret["error"] = "太短"
    except Exception as e:
        ret["status"] = False
        ret["error"] = "未知错误"

    return HttpResponse(json.dumps(ret))

def app(request):
    if request.method == "GET":
        app_list = models.Application.objects.all()
        host_list = models.Host.objects.all()
        return render(request, "app.html", {"app_list": app_list,"host_list":host_list})
    elif request.method == "POST":
        name = request.POST.get("app",None)
        host_list = request.POST.getlist("host_list",None)
        obj = models.Application.objects.create(name=name)
        obj.r.add(*host_list)
        return redirect("/app")

def add_adjax(request):
    ret = {"status":True,"error":None,"data":None}
    name = request.POST.get("app",None)
    host_list = request.POST.getlist("host_list",None)
    obj = models.Application.objects.create (name=name)
    obj.r.add (*host_list)
    print(host_list)
    return HttpResponse(json.dumps(ret))
