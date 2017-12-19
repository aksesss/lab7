"""test5_full URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from myapp.views import *
# from django.conf.urls import include, url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^main/', mainView, name="main_url"),
    url(r'^goods/$', GoodsListView.as_view(), name="goods_url"),
    url(r'^info/$', infoView, name="info_url"),
    url(r'^goods/add/$', goodsAddView, name="goods_add_url"),

    url(r'^register/$', RegisterFormView.as_view(), name="reg1"),
    url(r'^reg/$', registrationmy, name="reg_my_url"),
    url(r'^login/$', LoginFormView.as_view(), name="login_url"),
    url(r'^logout/$', LogoutView.as_view(), name="logout_url"),
    url(r'^qqq/$', RegisterFormView.as_view(), name="llogout_url"),


    url(r'^$', LoginFormView.as_view()),



]
