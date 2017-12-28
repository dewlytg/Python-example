from django.shortcuts import render,redirect,HttpResponse
from app01 import models
# Create your views here.
def login(request):
    if request.method == "GET":
        return render(request,"login.html")
    else:
        u = request.POST.get("user")
        p = request.POST.get("pwd")
        if u == "root" and p == "123":
            request.session["username"] = u
            request.session["is_login"] = True
            if request.POST.get("rmb",None) == "1":
                request.session.set_expiry(10)
            return redirect("/index")
        else:
            return render(request, "login.html")

def index(request):
    if request.session.get("is_login",None):
        return render(request,"index.html")
    else:
        return HttpResponse("get out!")

def logout(request):
    request.session.clear()
    return redirect("/login")


class Foo:
    def render(self):
        return HttpResponse ("Ok")

def test(request):
    # int("abc")
    print("请求来了")
    return Foo()

from django.views.decorators.cache import cache_page

# 此网页缓存
@cache_page(3)
def cache(request):
    import time
    ctime = time.time()
    return render(request,"cache.html",{"ctime":ctime})

def signal(request):
    u1 = models.UserInfo(name="u1")
    print("end")
    u1.save()

    u2 = models.UserInfo(name="u2")
    u2.save()

    u3 = models.UserInfo(name="u3")
    u3.save()

    # 触发自定义信号
    from sg import pizza_done
    pizza_done.send(sender='seven', toppings=123, size=456)
    return HttpResponse("Ok")

from django import forms
from django.forms import widgets,fields
class FM(forms.Form):
    user = fields.CharField(error_messages={"required":"用户名不能为空"},widget=widgets.Textarea(attrs={"class":"c1"}),label="用户名",initial="abc")
    pwd = fields.CharField(min_length=6,max_length=12,error_messages={"min_length":"最少六位","max_length":"最长12位"},widget=widgets.PasswordInput(attrs={"class":"c2"}))
    email = fields.EmailField(error_messages={"required":"邮箱不能为空","invalid":"邮箱格式不对"})
    f = fields.FileField()
    p = fields.FilePathField(path="app01")
    city1 = fields.ChoiceField(choices=[(1,"北京"),(2,"上海"),(3,"广州")])
    city2 = fields.MultipleChoiceField(choices=[(1,"北京"),(2,"上海"),(3,"广州")])

def fm(request):
    dic = {
        "user":"root",
        "pwd":"123",
        "email":"e@cutt.com",
        "city1":1,
        "city2":[1,2]
    }

    if request.method == "GET":
        obj = FM(dic)
        return render(request,"fm.html",{"obj":obj})
    elif request.method == "POST":
        obj = FM(request.POST)
        if obj.is_valid():
            print(obj.cleaned_data)
            models.UserInfo.objects.create(**obj.cleaned_data)
        else:
            return render(request, "fm.html", {"obj": obj})
        return render(request,"fm.html")