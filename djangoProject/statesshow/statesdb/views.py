from django.shortcuts import render
from statesdb import models
# Create your views here.
# 编写业务逻辑views
from django.shortcuts import HttpResponse

def index(request):
    # return HttpResponse("hello world!haaaaaaaaaa")
    # return render(request, "index.html")
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
    return render(request, "index.html", {"data": user_list})

def index2(request):
    # return HttpResponse("hello world!haaaaaaaaaa")
    return render(request, "index2.html")