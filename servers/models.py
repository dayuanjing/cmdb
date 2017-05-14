# -*- coding: utf-8 -*-：
from django.db import models

# Create your models here.


class IdcGroup(models.Model):
    idc_name = models.CharField(max_length=100)     # idc名字
    idc_address = models.CharField(max_length=100)  # idc地址
    idc_phone = models.CharField(max_length=10)     # idc客服电话
    idc_email = models.EmailField()                 # 邮箱地址
    remarks = models.TextField(blank=True)          # 备注
    create_time = models.DateTimeField()            # 创建时间

    def __unicode__(self):
        return self.idc_name


class ItemGroup(models.Model):
    item_name = models.CharField(max_length=20)  # 项目组名称
    remarks = models.TextField(blank=True)  # 备注
    create_time = models.DateTimeField()  # 创建时间

    def __unicode__(self):
        return self.item_name


class ServerInfo(models.Model):
    server_ip = models.GenericIPAddressField()  # 服务器IP
    server_number = models.CharField(max_length=30)  # 快速服务编号
    server_delivery_date = models.DateField()  # 服务器发货日期 2014/5/4
    server_version = models.CharField(max_length=50)  # 服务器型号
    cpu_version = models.CharField(max_length=100)  # CPU型号
    cpu_count = models.IntegerField()  # CPU物理个数
    cpu_cores = models.IntegerField()  # Cpu核数
    cpu_processor = models.IntegerField()  # Cpu逻辑个数
    memory = models.FloatField()  # 内存大小
    disk = models.FloatField()  # 硬盘大小
    idc_group = models.ForeignKey(IdcGroup)  # 所属机房
    item_group = models.ForeignKey(ItemGroup)  # 所属组
    create_time = models.DateTimeField()  # 创建时间

    def __unicode__(self):
        return self.server_number


class ServerHistoryInfo(models.Model):
    server_number = models.ForeignKey(ServerInfo)  # 快速服务编号 与ServerInfo多对一
    h_server_ip = models.GenericIPAddressField()  # 服务器IP
    h_cpu_version = models.CharField(max_length=100)  # CPU型号
    h_cpu_count = models.IntegerField()  # CPU物理个数
    h_cpu_cores = models.IntegerField()  # Cpu核数
    h_cpu_processor = models.IntegerField()  # Cpu逻辑个数
    h_memory = models.FloatField()  # 内存大小
    h_disk = models.FloatField()  # 硬盘大小
    h_idc_group = models.CharField(max_length=10)  # 所属机房
    h_item_group = models.CharField(max_length=10)  # 所属组
    update_time = models.DateTimeField()  # 变更时间

    def __unicode__(self):
        return self.server_number
