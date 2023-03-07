"""coats_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from coatsapp import views
from coatsapp.views import index,ManagerAPIView,adminpage,Get_samp,dashboard,Get_Predtime,Get_machine,Get_packing,Get_attendance,labour,order,Machine,Predtime_page,first_machine,packing

urlpatterns = [
    path('admin', admin.site.urls),
    path('Manager_login', ManagerAPIView.as_view()),
    path(r'JAN', views.JANAPIView.as_view(), name='jan-list'),
    path(r'Employee', views.EmployeeAPIView.as_view(), name='Employee-list'),
    path(r'Machine', views.MachineAPIView.as_view(), name='Machine-list'),
    path(r'Manager', views.ManagerAPIView.as_view(), name='Manager-list'),
    path(r'MaterialFinish', views.MaterialFinishAPIView.as_view(), name='Material-list'),
    path(r'order', views.place_orderAPIView.as_view(), name='Placeorder-list'),
    path('index',index),
    path('labour',labour),
    path('order_p',order),
    path('packing_p',packing),
    path('Machine_p',Machine),
    path('predtime_p',Predtime_page),
    path('adminpage',adminpage),
    path('dashboard',dashboard),
    path('first_machine',first_machine),
    path('get_pred',Get_samp),
    path('get_predtime',Get_Predtime),
    path('get_machine',Get_machine),
    path('get_packing',Get_packing),
    path('get_attendance',Get_attendance),
]
