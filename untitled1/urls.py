"""untitled1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app01 import views as app01

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^$", app01.index),
    url(r"^accounts/login/$", app01.acc_login),
    url(r"^accounts/logout/$", app01.acc_logout),
    url(r'^ip/', app01.ip),
    url(r'^business_daily_traffic/', app01.Business_daily_traffics),
    url(r'^heat_chart/', app01.Heat_chart),
    url(r'^real_time/', app01.real_time),
    url(r'^Big_picture', app01.Big_picture),
    url(r'^total_rmb', app01.total_rmb),
    url(r'^first_10', app01.first_10),
    url(r'^first10_1', app01.first10_1),
    url(r'^City_trading_volume', app01.City_trading_volumes),
    url(r'^business_real_time_accesss/', app01.business_real_time_accesss),
    url(r'^pie_custom/', app01.pie_custom,name='pie_custom'),
    url(r'^tables/', app01.tables,name='tables'),

    url(r'^add', app01.add),
    url(r'^ajax_dict/$', app01.ajax_dict),
    #####ajax####
    url(r'^real_time_time_list/$', app01.real_time_time_list),
    url(r"^business_real_time_accesss_ajax", app01.business_real_time_accesss_ajax),
    url(r'^Heat_chart_ajax/', app01.Heat_chart_ajax),
]
