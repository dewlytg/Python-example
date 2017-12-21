from django.conf.urls import url,include
from app02 import views

urlpatterns = [
    url(r'business',views.business),

    url(r'^/host$',views.host),
    url(r'^/add_ajax_host$',views.add_ajax_host),
    url(r'^/edit_host$',views.edit_host),
    url(r'^/del_host$',views.del_host),

    url(r'^/app$',views.app),
    url(r'^/add_ajax_app$',views.add_ajax_app),
    url(r'^/edit_app$',views.edit_app),
    url(r'^/del_app$',views.del_app),
]