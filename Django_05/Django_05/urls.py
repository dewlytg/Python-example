"""Django_05 URL Configuration

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
    path('admin/', admin.site.urls),
    url(r'index$', views.index),
    url(r'register$', views.register),
    url(r'login$', views.login),
    url(r'sysadm$', views.sysadm),
    url(r'hostlist$', views.hostlist),
    url(r'^addhost$', views.addhost),
    url(r'^ajaxaddhost$', views.ajaxaddhost),
    url(r'^edithost$', views.edithost),
    url(r'^delhost$', views.delhost),
    url(r'^manydelhost$', views.manydelhost),
    url (r'^order$', views.Order.as_view()),
    url(r'^test$', views.test),
    url(r'^application$', views.application),
    url(r'^addapp', views.addapp),
    url(r'^editapp', views.editapp),
    url(r'^delapp', views.delapp),
]
