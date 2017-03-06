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
    url(r'^ip/',app01.ip),
    url(r'^business_daily_traffic/',app01.Business_daily_traffics),
    url(r'^heat_chart/',app01.Heat_chart),
    url(r'^$',app01.index),
    url(r'^real_time/',app01.real_time),
    url(r"^accounts/login/",app01.login),
    url(r"^accounts/logout/",app01.acc_logout),
]
