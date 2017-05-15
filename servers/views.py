# coding=utf-8
from django.shortcuts import render
from .models import ServerInfo, IdcGroup, ItemGroup
from django.http import HttpResponse


# Create your views here.
def server_list(request):
    all_servers = ServerInfo.objects.all()
    if all_servers:
        return render(request, 'servers/server_list.html', {'all_servers': all_servers})
    else:
        message = u"没有服务器数据！"
        return render(request, 'servers/server_list.html', {'message': message})


def idc_list(request):
    all_idc = IdcGroup.objects.all()
    if all_idc:
        return render(request, 'servers/idc_list.html', {'all_idc': all_idc})
    else:
        message = u"没有机房数据！"
        return render(request, 'servers/idc_list.html', {'message': message})


def item_list(request):
    all_item = ItemGroup.objects.all()
    if all_item:
        return render(request, 'servers/item_list.html', {'all_item': all_item})
    else:
        message = u"没有项目组数据！"
        return render(request, 'servers/item_list.html', {'message': message})


def idc_add(request):
    return render(request, 'servers/idc_add.html')


def item_add(request):
    return render(request, 'servers/item_add.html')


def servers_add(request):
    return render(request, 'servers/server_add.html')

