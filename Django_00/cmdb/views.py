from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from cmdb.models import HostInfo,UserInfo

# Create your views here.

def login(request):
    # 第一种方法，问题是写在逻辑页面这里不符合规范
    # string = """
    # <form>
    #     <input type="text">
    # </form>
    # """

    # 第二种方法，问题是每个客户端链接的时候都会有一个文件打开
    # f = open("templates/login.html","r",encoding="utf-8")
    # data = f.read()
    # f.close()
    # return HttpResponse(data)

    # 第三种方法
    # return render(request,"login.html")

    # 通过request获取用户的请求方式
    # print(request.method)
    error_msg = ""
    if request.method == "POST":
        user = request.POST.get("user",None)
        pwd = request.POST.get("pwd",None)
        obj = UserInfo.objects.get(username=user)
        if user == obj.username and pwd == obj.pwd:
            # 如果用户名和密码正确，跳转
            return redirect("/hostinfo")
        else:
            error_msg = "用户名密码错误"

    return render(request,"login.html",{"error_msg":error_msg})

# def home(request):
#     return HttpResponse("<h1>CMDB</h1>")

USER_LIST = [
    {"username":"zs","password":"123","email":"zs@163.com"},
    {"username":"ls","password":"123","email":"ls@163.com"},
    {"username":"we","password":"123","email":"we@163.com"}
]

def home(request):
    if request.method == "POST":
        u = request.POST.get("user",None)
        p = request.POST.get("pwd",None)
        e = request.POST.get("email",None)
        temp = {"username":u,"password":p,"email":e}
        USER_LIST.append(temp)
    return render(request,"home.html",{"user_list":USER_LIST})

def getHostAll():
    hostlist = []
    hostinfo = HostInfo.objects.all()
    for host in hostinfo:
        id = host.id
        hostname = host.hostname
        position = host.position
        osname = host.osname
        hostdict = {"id": id, "hostname": hostname, "position": position, "osname": osname}
        hostlist.append(hostdict)
    return hostlist

def hostinfo(request):
    if request.method == "POST":
        id = request.POST.get("id",None)
        hostname = request.POST.get("hostname",None)
        position = request.POST.get("position",None)
        osname = request.POST.get("osname",None)
        record = HostInfo.objects.get(id=id)
        print(hostname,position,osname)
        record.hostname = hostname
        record.position = position
        record.osname = osname
        record.save()
        hostlist = getHostAll()
    else:
        id = request.GET.get("did",None)
        if id:
            HostInfo.objects.filter(id=id).delete()
        else:
            print("normal display !")
        hostlist = getHostAll()

    return render(request, "hostinfo.html", {"hostlist": hostlist})



