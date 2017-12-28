"""Django_04 URL Configuration

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
from django.urls import path,include
from django.conf.urls import url
from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'index', views.index,{"name":"root"}),
    # url(r'a/', include("app01.urls",namespace="authors")),
    url(r'tpl1', views.tpl1),
    url(r'tpl2', views.tpl2),
    url(r'tpl3', views.tpl3),
    url(r'tpl4', views.tpl4),
    url(r'user_list', views.user_list),
    url(r'login', views.login),
    url(r'index', views.index),
    url(r'order', views.Order.as_view()),
]
