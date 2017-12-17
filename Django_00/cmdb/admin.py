from django.contrib import admin
from cmdb import models
# Register your models here.

## django提供的后台管理
admin.site.register(models.UserInfo)
admin.site.register(models.UserType)
admin.site.register(models.HostInfo)