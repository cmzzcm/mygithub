from django.shortcuts import render

# Create your views here.
# 编写业务逻辑views
from django.shortcuts import HttpResponse

def index(request):
    # return HttpResponse("hello world!haaaaaaaaaa")
    return render(request, "index.html")

def UI_Dots(request):
    return render(request, "UI_Dots.html")

# def myview(request):
#    return HttpResponseRedirect("/path/")

def B3F3(request):
    return render(request, "B3F3.html")

def CarDesign(request):
    return render(request, "CarDesign.html")

def ChargingBarrel(request):
    return render(request, "ChargingBarrel.html")

def COURSERA(request):
    return render(request, "COURSERA.html")

def Drawing_Car(request):
    return render(request, "Drawing_Car.html")

def Drawing_Rainyday(request):
    return render(request, "Drawing_Rainyday.html")

def DustBlowing(request):
    return render(request, "DustBlowing.html")

def IconSmartisan(request):
    return render(request, "IconSmartisan.html")

def MultidimensionalMixer(request):
    return render(request, "MultidimensionalMixer.html")

def OverallEffect_Byhealth(request):
    return render(request, "OverallEffect_Byhealth.html")

def Poster_dayuhaitang(request):
    return render(request, "Poster_dayuhaitang.html")

def poster_Halloween(request):
    return render(request, "poster_Halloween.html")

def RunningWater(request):
    return render(request, "RunningWater.html")

def UI_Record(request):
    return render(request, "UI_Record.html")

def UI_Skiing(request):
    return render(request, "UI_Skiing.html")

def UI_Yoga(request):
    return render(request, "UI_Yoga.html")

def WEBbanner(request):
    return render(request, "WEBbanner.html")

def UI_JustMusic_detail(request):
    return render(request, "UI_JustMusic_detail.html")
