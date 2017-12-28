from django.shortcuts import render,HttpResponse,redirect
from django.utils.safestring import mark_safe
from django.views import View
from django.utils.decorators import method_decorator
from app01 import models
from app01.utils.pagination import Page
import re,json

u_str = r"^\d{11}$"

# Create your views here.
def index(request):
    return render(request,"index.html")

def register(request):
    ret = {"status":True,"error":None,"data":None}
    u_str = r"^\d{11}$"
    p_str = r"^\w{3,6}$"
    e_str = r"\w+@\w+\.\w+"
    if request.method == "GET":
        return redirect("/index")
    elif request.method == "POST":
        u = request.POST.get("user",None)
        p = request.POST.get("pwd",None)
        pto = request.POST.get("pwdto",None)
        e = request.POST.get("email",None)
        if re.match(u_str,u) and re.match(p_str,p) and re.match(e_str,e) and p == pto:
            obj = models.User.objects.filter(username=u).first()
            if obj:
                ret["status"] = False
                ret["error"] = "用户已存在"
                return HttpResponse (json.dumps (ret))
            else:
                ret["data"] = "注册成功"
                models.User.objects.create(username=u,pwd=p,email=e)
                return HttpResponse(json.dumps(ret))
        else:
            ret["status"] = False
            ret["error"] = "格式不对"
            return HttpResponse(json.dumps(ret))

def login(request):
    # $.ajax()登录方式
    # ret = {"status": True, "error": None, "data": None}
    # u = request.POST.get("user",None)
    # p = request.POST.get("pwd",None)
    # print(u,p)
    # if models.User.objects.filter(username=u,pwd=p):
    #     ret["data"] = "登录成功"
    # else:
    #     ret["status"] = False
    #     ret["error"] = "用户名密码错误"
    # return HttpResponse(json.dumps(ret))

    #新页面登录方式
    u = request.POST.get("user",None)
    p = request.POST.get("pwd",None)
    if models.User.objects.filter(username=u,pwd=p):
        res = redirect("/sysadm")
        res.set_cookie("username",u)
        return res
    else:
        return render(request,"index.html")

def sysadm(request):
    v = request.COOKIES.get("username",None)
    if v:
        return render(request,"sysadm.html")
    else:
        return redirect("/index")

def auth(func):
    def inner(request,*args,**kwargs):
        username = request.COOKIES.get("username", None)
        if username:
            return func(request,*args,**kwargs)
        else:
            return redirect("/login")
    return inner

@auth
def hostlist(request):
    hostgroup_list = models.HostGroup.objects.all()
    username = request.COOKIES.get("username", None)
    current_page = int(request.GET.get("p",1))
    pagination_nums = int(request.COOKIES.get("pagination_nums",20))
    obj = Page(current_page,pagination_nums)
    data = obj.get_hostlist
    page_str = mark_safe("".join(obj.get_str("/hostlist")))
    return render(request,"hostlist.html",{"host_list":data,"page_str":page_str,"username":username,"hostgroup_list":hostgroup_list})

def addhost(request):
    if request.method == "GET":
        pass
    elif request.method == "POST":
        hostname = request.POST.get("hostname",None)
        ip = request.POST.get("ip",None)
        port = request.POST.get("port",None)
        g_id = request.POST.get("g_id",None)
        ret = [hostname,ip,port,g_id]
        if all(ret):
            models.Host.objects.create(hostname=hostname,ip=ip,port=port,g_id=g_id)
        else:
            pass
        return redirect("/hostlist")

def ajaxaddhost(request):
    ret = {"status":True,"error":None,"data":None}
    if request.method == "GET":
        pass
    elif request.method == "POST":
        try:
            hostname = request.POST.get ("hostname", None)
            ip = request.POST.get ("ip", None)
            port = request.POST.get ("port", None)
            g_id = request.POST.get ("g_id", None)
            if len (hostname) < 5:
                ret["status"] = False
                ret["error"] = "主机名太短"
            else:
                ret["data"] = "添加成功"
                models.Host.objects.create(hostname=hostname, ip=ip, port=port, g_id=g_id)
        except Exception as e:
            ret["status"] = False
            ret["error"] = "未知错误"
        return HttpResponse(json.dumps(ret))


def edithost(request):
    if request.method == "GET":
        pass
    elif request.method == "POST":
        h_id = request.POST.get("h_id",None)
        hostname = request.POST.get("hostname",None)
        ip = request.POST.get("ip",None)
        port = request.POST.get("port",None)
        g_id = request.POST.get("g_id",None)
        ret = [hostname,ip,port,g_id]
        if all(ret):
            obj = models.Host.objects.filter(id=h_id)
            obj.update(hostname=hostname,ip=ip,port=port,g_id=g_id)
        else:
            pass
        return redirect("/hostlist")

def delhost(request):
    if request.method == "GET":
        pass
    elif request.method == "POST":
        h_id = request.POST.get("h_id",None)
        models.Host.objects.filter(id=h_id).delete()
        return redirect("/hostlist")

def manydelhost(request):
    del_list = request.POST.getlist("del_list",None)
    for i in del_list:
        models.Host.objects.filter(id=i).delete()
    return HttpResponse("删除成功")

@method_decorator(auth,name="dispatch")
class Order(View):

    # @method_decorator(auth)
    # def dispatch(self, request, *args, **kwargs):
    #     return super(Order,self)(request, *args, **kwargs)

    # @method_decorator(auth)
    def get(self,request):
        username = request.COOKIES.get("username")
        return render(request, "index.html", {"username": username})

    def post(self,request):
        username = request.COOKIES.get("username")
        return render (request, "index.html", {"username": username})

def application(request):
    applist = models.Applicaton.objects.all()
    hostlist = models.Host.objects.all()
    return render(request,"application.html",{"applist":applist,"hostlist":hostlist})

def addapp(request):
    appname = request.POST.get("appname",None)
    hostlist = request.POST.getlist("host_list",None)
    obj = models.Applicaton.objects.create(name=appname)
    obj.h.add(*hostlist)
    return redirect("/application")

def editapp(request):
    appid = request.POST.get("appid",None)
    appname = request.POST.get("appname",None)
    host_list = request.POST.getlist("host_list",None)
    obj = models.Applicaton.objects.filter(id=appid).first()
    obj.name = appname
    obj.save()
    obj.h.set(host_list)
    return redirect("/application")

def delapp(request):
    appid = request.POST.get ("appid", None)
    obj = models.Applicaton.objects.filter(id=appid).first()
    obj.h.clear()
    models.Applicaton.objects.filter(id=appid).delete()
    return HttpResponse("删除成功")

def test(request):
    # import random
    # for i in range(100):
    #     gid = random.choice([x for x in range(1,9)])
    #     hostname = "server00" + str(i)
    #     port = 80
    #     ip = "1.1.1.1"
    #     models.Host.objects.create(hostname=hostname,ip=ip,port=port,g_id=gid)
    # models.Host.objects.all().delete()
    return HttpResponse("add host list")