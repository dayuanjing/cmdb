# -*- coding: utf-8 -*-：
from django.shortcuts import render
from django.http import HttpResponse
from .models import User


# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        re = User.objects.filter(username=username, password=password)
        if re:
            message = u"欢迎您:" + username
            return render(request, 'home.html', {'message': message})
        else:
            error_messge = u"用户名或密码错误"
            return render(request, 'index.html', {'error_messge': error_messge})
    else:
        return render(request, 'index.html')

