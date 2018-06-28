from django.shortcuts import render
from django.shortcuts import HttpResponse
from catdb import models
from django.http import HttpResponseRedirect

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def login(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")


# Create your views here.
def index1(request):
    # return HttpResponse("hei man!")
    user_list = []
    # models.UserInfo.objects.create(user='rose', pwd='123456')   # 增加一条数据
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        # # print(username, password)
        # 添加数据到数据库
        models.UserInfo.objects.create(user=username, pwd=password)
        # 从数据库中读取所有数据# 读取所有行
        user_list = models.UserInfo.objects.all()
        # 从数据库删除

        # 设置返回templates返回的页面
    return render(request, "index1.html", {"data": user_list})

def deluser(request):
    id = request.GET.get('id')
    models.UserInfo.objects.filter(user='id').delete()
    # return HttpResponseRedirect('/index/')
    # 从数据库中读取所有数据# 读取所有行
    user_list = models.UserInfo.objects.all()
    return render(request, "index1.html", {"data": user_list})

def rearch(request):
    # 从数据库中读取所有数据# 读取所有行
    user_list = models.UserInfo.objects.all()
    return render(request, 'index1.html', {"data": user_list})