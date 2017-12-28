from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.urls import reverse
from django.utils.safestring import mark_safe
# Create your views here.
from utils import pagination

# def index(request):
#     print(reverse("authors:index"))
#     return HttpResponse("OK")

def tpl1(request):
    u_list = ["zhao","qian","sun","wu"]
    return render(request,"tpl1.html",{"u":u_list})

def tpl2(request):
    msg = "修改密码"
    return render(request,"tpl2.html",{"msg":msg})

def tpl3(request):
    status = "用户删除"
    return render(request,"tpl3.html",{"status":status})

def tpl4(request):
    username = "JAMES"
    return render(request,"tpl4.html",{"username":username})

def user_list(request):
    LIST = [i for i in range(500)]
    current_page = int(request.GET.get("p",1))

    per_page_count = int(request.COOKIES.get("per_page_count",None))

    page_obj = pagination.Page(current_page,len(LIST),per_page_count)
    data = LIST[page_obj.start:page_obj.end]
    page_str = mark_safe("".join(page_obj.page_str("/user_list"))) # 防止XXS
    return render(request,"user_list.html",{"user_list":data,"page_str":page_str})

user_info = {
    "zhangsan":{"pwd":"123123"},
    "lisi":{"pwd":"123123"},
}

def login(request):
    if request.method == "GET":
        return render(request,"login.html")
    if request.method == "POST":
        u = request.POST.get("username",None)
        p = request.POST.get("pwd",None)
        if not user_info.get("u",None):
            if user_info[u]["pwd"] == p:
                ret = redirect("/index")
                # 给客户端浏览器设置cookie
                # ret.set_cookie("username",u)
                # max_age 设置cookie的过期时间
                # ret.set_cookie("username",u,max_age=10)
                # import datetime
                # current_date = datetime.datetime.utcnow()
                # expires也是设置过期时间
                # current_date = current_date + datetime.timedelta(seconds=10)
                # ret.set_cookie("username",u,expires=10)
                ret.set_cookie("username",u)
                # httponly设置只能在http的请求的cookie中看到,document.cookies 不能获取
                ret.set_cookie("http_msg","abc",httponly=True)
                # set_signed_cookie 加密cookie,salt="加密字符串",机密也要用这个字符串
                # ret.set_signed_cookie(salt="abcdefg")
                # request.get_signed_cookie(salt="abcdefg")
                return ret
            else:
                return render(request, "login.html")
        else:
            return render(request, "login.html")

def auth(func):
    def inner(request,*args,**kwargs):
        username = request.COOKIES.get("username")
        if not username:
            return redirect("/login")
        return func(request,*args,**kwargs)
    return inner

@auth
def index(request):
    username = request.COOKIES.get("username")
    return render(request, "index.html", {"username": username})

from django.views import View
from django.utils.decorators import method_decorator

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