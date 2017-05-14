# -*- coding: utf-8 -*-：
from django.db import models


# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=100)  # 用户名
    password = models.CharField(max_length=20)  # 密码

    def __unicode__(self):
        return self.username
