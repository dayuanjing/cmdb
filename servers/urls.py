from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.server_list, name='server_list'),
    url(r'^idc/$', views.idc_list, name='idc_list'),
    url(r'^item/$', views.item_list, name='item_list'),
    url(r'^add/$', views.servers_add, name='servers_add'),
    url(r'^idc/add/$', views.idc_add, name='idc_add'),
    url(r'^item/add/$', views.item_add, name='item_add'),
]
