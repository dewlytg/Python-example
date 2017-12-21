
from django.conf.urls import url,include
from app01 import views

urlpatterns = [
    url(r'business$',views.business ),
    url(r'host$',views.host ),
    url(r'test_ajax$',views.test_ajax ),
    url(r'app$',views.app ),
    url(r'add_adjax$',views.add_adjax ),
]