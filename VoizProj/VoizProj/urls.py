"""VoizProj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.contrib import admin
from django.urls import path
from VoizProj.routers import router
from VoizApp import views

from django.urls import include, path
from rest_framework import routers
from VoizApp.views import plan, number, account, dueamt,prepaid, postpaid, dongle, recharge
from VoizApp.viewsets import numberVS, planVS, accountVS, dueamtVS,prepaidVS, postpaidVS, dongleVS, rechargeVS

router = routers.DefaultRouter()
router.register('list', numberVS, basename='list')
router.register('list1', planVS, basename='list1')
router.register('list2', accountVS, basename='list2' )
router.register('list3', dueamtVS, basename='list3')
router.register('list4', prepaidVS, basename='list4')
router.register('list5', postpaidVS, basename='list5')
router.register('list6', dongleVS, basename='list6')
router.register('list7', rechargeVS, basename='list7')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('viewplans/',views.viewplans, name ="viewplans"),
    path('offers/',views.offers, name ="offers"),
    path('home/',views.home, name ="home"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('recharge/', views.recharge, name="recharge"),
    path('issues/',views.issues, name ="issues"),
    path('invoice/',views.invoice, name ="invoice"),
    path('invoice1/',views.invoice1, name ="invoice"),
    path('adminhome/',views.adminhome, name ="adminhome"),
]
