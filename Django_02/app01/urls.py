"""Django_02 URL Configuration

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
from django.conf.urls import url
from app01 import views

urlpatterns = [
    path('login', views.login),
    path('backend', views.backend),
    path('user_info', views.user_info),
    url(r'user_detail-(?P<uid>\d+).html', views.user_detail),
    url(r'user_del-(?P<uid>\d+).html', views.user_del),
    url(r'user_edit-(?P<uid>\d+).html', views.user_edit),

    url(r'usergroup_info', views.usergroup_info),
    url(r'usergroup_detail-(?P<gid>\d+).html', views.usergroup_detail),
    url(r'usergroup_del-(?P<gid>\d+).html', views.usergroup_del),
    url(r'usergroup_edit-(?P<gid>\d+).html', views.usergroup_edit),

    # orm专门测试用的页面
    path('orm', views.orm),
]