from django.contrib import admin
from .models import ServerHistoryInfo, ServerInfo, IdcGroup, ItemGroup


# Register your models here.

class ServerInfoAdmin(admin.ModelAdmin):
    list_display = ('server_number', 'server_ip', 'server_delivery_date', 'server_version')


admin.site.register(ServerHistoryInfo)
admin.site.register(ServerInfo, ServerInfoAdmin)
admin.site.register(IdcGroup)
admin.site.register(ItemGroup)
