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
from django.conf.urls import url,include

urlpatterns = [
    path ('admin/', admin.site.urls),
    path('cmdb/', include("app01.urls")),
    path('monitor/', include("app02.urls")),
]


"""
urlpatterns = [
    path('admin/', admin.site.urls),
    # url('^index', views.index),
    # url('^indexaaaaaaaaabbbbbbbccccccc/', views.index ,name="index"),
    # url('^indexaaaaaaaaabbbbbbbccccccc/(\d+)', views.index ,name="index"),
    # url('^indexaaaaaaaaabbbbbbbccccccc/(\d+)/(\d+)', views.index ,name="index"),
    url('^indexaaaaaaaaabbbbbbbccccccc/(?P<nid>\d+)/(?P<uid>\d+)', views.index ,name="index"),
    url('^home', views.home),
    url('^login', views.Login.as_view()),
    url('^detail-(\d+).html', views.detail),
    # url('^detail-(\d+)-(\d+).html', views.detail),
    # url('^detail-(?P<nid>\d+)-(?P<uid>\d+).html', views.detail),
]
"""