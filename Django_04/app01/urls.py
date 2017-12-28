from django.conf.urls import url
from app01 import views
app_name = "app01"

urlpatterns = [
    url(r'index', views.index,name="index"),
]
