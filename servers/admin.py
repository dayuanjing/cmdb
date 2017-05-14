from django.contrib import admin
from .models import ServerHistoryInfo, ServerInfo, IdcGroup, ItemGroup


# Register your models here.
admin.site.register(ServerHistoryInfo)
admin.site.register(ServerInfo)
admin.site.register(IdcGroup)
admin.site.register(ItemGroup)
