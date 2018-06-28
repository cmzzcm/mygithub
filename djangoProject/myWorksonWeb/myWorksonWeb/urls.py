"""myWorksonWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webdb import views
from django.conf.urls import url

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^index', views.index),
    url(r'^UI_Dots', views.UI_Dots),
	url(r'^UI_JustMusic_detail', views.UI_JustMusic_detail),
	url(r'^B3F3', views.B3F3),
    url(r'^CarDesign', views.CarDesign),
	url(r'^ChargingBarrel', views.ChargingBarrel),
	url(r'^COURSERA', views.COURSERA),
    url(r'^Drawing_Car', views.Drawing_Car),
	url(r'^Drawing_Rainyday', views.Drawing_Rainyday),
	url(r'^DustBlowing', views.DustBlowing),
    url(r'^IconSmartisan', views.IconSmartisan),
	url(r'^MultidimensionalMixer', views.MultidimensionalMixer),
	url(r'^OverallEffect_Byhealth', views.OverallEffect_Byhealth),
    url(r'^Poster_dayuhaitang', views.Poster_dayuhaitang),
	url(r'^poster_Halloween', views.poster_Halloween),
	url(r'^RunningWater', views.RunningWater),
    url(r'^UI_Record', views.UI_Record),
	url(r'^UI_Skiing', views.UI_Skiing),
	url(r'^UI_Yoga', views.UI_Yoga),
	url(r'^WEBbanner', views.WEBbanner),
]