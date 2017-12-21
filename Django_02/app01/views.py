from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.views import View
import os
from app01 import models
# Create your views here.

USER_DICT = {
    "1":{"name":"root1","email":"root1@163.com"},
    "2":{"name":"root2","email":"root2@163.com"},
    "3":{"name":"root3","email":"root3@163.com"},
    "4":{"name":"root4","email":"root4@163.com"},
    "5":{"name":"root5","email":"root5@163.com"},
}

def index(request,nid,uid):
    # print(request.path_info)
    from django.urls import reverse
    # 此处的index为url中定义的name
    # u1 = reverse("index",args=(1,))
    # u1 = reverse("index",args=(nid,))
    # u2 = reverse("index",args=(nid,uid))
    u3 = reverse("index",kwargs={"nid":nid,"uid":uid})
    # print(u3)
    return render(request,"index.html",{"userdict":USER_DICT})

def home(request):
    if request.method == "GET":
        print(request.method)
        return render(request,"home.html")
    elif request.method == "POST":
        # 获取请求方式
        # print(request.method,"POST")

        # 获取单个值
        # u = request.POST.get("user",None)
        # p = request.POST.get("pwd",None)
        # g = request.POST.get("gender",None)

        # 获取多个值
        # f = request.POST.getlist("favior",None)
        # c = request.POST.getlist("city",None)
        # print(u,p,g,f,c)

        # 获取文件内容
        obj = request.FILES.get("uploadfile",None)
        fname = os.path.join("upload",obj.name)
        f = open(fname,mode="wb")
        for row in obj.chunks():
            f.write(row)
        f.close()
        return render(request,"home.html")
    else:
        pass

class Login(View):
    def dispatch(self, request, *args, **kwargs):
        print("before")
        result = super(Login,self).dispatch(request, *args, **kwargs)
        print("after")
        return result

    def get(self,request):
        return render(request,"login.html")

    def post(self,request):
        return render (request, "login.html")

def detail(request,nid):
    # url('^detail-(\d+)-(\d+).html', views.detail),
    # detail(request,nid,uid)

    # url('^detail-(?P<nid>\d+)-(?P<uid>\d+).html', views.detail),
    # detail(request,nid,uid)
    detail_info = USER_DICT[nid]
    return render(request,"detail.html",{"detail_info":detail_info})

def login(request):
    if request.method == "GET":
        return render(request,"login.html")
    elif request.method == "POST":
        u = request.POST.get("user",None)
        p = request.POST.get("pwd",None)
        # QuerySet 类型
        # models.UserInfo.objects.filter(username=u,password=p).count()
        obj = models.UserInfo.objects.filter(username=u,password=p).first()
        if obj:
            return redirect("/cmdb/backend")
        else:
            return render(request,"login.html")
    else:
        return redirect("index")


def backend(request):
    return render(request,"backend.html")

def user_info(request):
    if request.method == "GET":
        user_list = models.UserInfo.objects.all()
        group_list = models.UserGroup.objects.all()
        return render (request, "user_info.html", {"user_list": user_list,"group_list":group_list})
    elif request.method == "POST":
        u = request.POST.get("username",None)
        p = request.POST.get("password",None)
        g = request.POST.get("group_id",None)
        models.UserInfo.objects.create(username=u,password=p,user_group_id=g)
        return redirect("/cmdb/user_info")

def user_detail(request,uid):
    detailinfo = models.UserInfo.objects.filter(id=uid).first()
    # get获取单条数据
    # obj = models.UserInfo.objects.get(id=uid)
    return render(request,"user_detail.html",{"detailinfo":detailinfo})

def user_del(request,uid):
    models.UserInfo.objects.filter(id=uid).delete()
    return redirect("/cmdb/user_info")

def user_edit(request,uid):
    if request.method == "GET":
        useredit = models.UserInfo.objects.filter(id=uid).first()
        return render(request,"user_edit.html",{"useredit":useredit})
    elif request.method == "POST":
        uid = request.POST.get("id",None)
        user = request.POST.get("user",None)
        pwd = request.POST.get("pwd",None)
        models.UserInfo.objects.filter(id=uid).update(username=user,password=pwd)
        return redirect("/cmdb/user_info")

def usergroup_info(request):
    if request.method == "GET":
        usergroup_list = models.UserGroup.objects.all()
        return render(request,"usergroup_info.html",{"usergroup_list":usergroup_list})
    elif request.method == "POST":
        caption = request.POST.get("caption",None)
        models.UserGroup.objects.create(caption=caption)
        return redirect("/cmdb/usergroup_info")

def usergroup_detail(request,gid):
    user_list = models.UserInfo.objects.filter(user_group_id=gid)
    return render(request,"usergroup_detail.html",{"user_list":user_list})

def usergroup_del(request,gid):
    if models.UserInfo.objects.filter(user_group_id=gid):
        models.UserInfo.objects.filter (user_group_id=gid).delete()
    else:
        pass
    models.UserGroup.objects.filter(uid=gid).delete()
    return redirect("/cmdb/usergroup_info")

def usergroup_edit(request,gid):
    if request.method == "GET":
        usergroupedit = models.UserGroup.objects.filter(uid=gid).first()
        return render(request,"usergroup_edit.html",{"usergroupedit":usergroupedit})
    elif request.method == "POST":
        n = request.POST.get("caption",None)
        models.UserGroup.objects.filter(uid=gid).update(caption=n)
        return redirect("/cmdb/usergroup_info")

def orm(request):
    # 增
    # models.UserInfo.objects.create(username="root",password="123")
    # obj = models.UserInfo(username="alex",password="555")
    # obj.save()
    # dic = {"username":"eric","password":"111"}
    # models.UserInfo.objects.create(**dic)

    # 查
    # result = models.UserInfo.objects.all()
    # result = models.UserInfo.objects.filter(username="root")
    # result = models.UserInfo.objects.filter(username="root",password="123")
    # for row in result:
    #     print(row.id,row.username,row.password)

    # 删
    # models.UserInfo.objects.filter(username="root").delete()

    # 改
    # models.UserInfo.objects.all().update(password="666")
    # models.UserInfo.objects.filter(username="root").update(password="123321")

    # models.UserInfo.create(
    #     usernmae="root1",
    #     password="123",
    #     email="abc@163.com",
    #     user_group = models.UserGroup.objects.filter(id="1").first(),
    # )
    # 上面的方式也可以，其实user_group就是一个UserGroup对象
    # models.UserInfo.objects.create(
    #     username="root2",
    #     password="123",
    #     email="abc@163.com",
    #     user_group_id = "5"
    # )

    obj = models.UserInfo.objects.filter(id=5).first()
    print(obj)
    print(obj.username,obj.password,obj.email)
    print(obj.user_group)
    print(obj.user_group.uid,obj.user_group.caption)
    print(obj.user_group_id)
    return HttpResponse("ORM")
