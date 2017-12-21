from django.db import models

# Create your models here.

class UserType(models.Model):
    id = models.AutoField(primary_key=True,max_length=16)
    name = models.CharField(max_length=32)

class UserInfo(models.Model):
    id = models.AutoField(primary_key=True,max_length=16)
    username = models.CharField(max_length=30)
    pwd = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    user_type = models.ForeignKey(UserType,on_delete=models.DO_NOTHING,)

class HostInfo(models.Model):
    id = models.AutoField(primary_key=True,max_length=16)
    hostname = models.CharField(max_length=32)
    ip = models.GenericIPAddressField(max_length=32)
    status = models.CharField(max_length=16)
    position = models.CharField(max_length=8)
    vendor = models.CharField(max_length=32)
    cputype = models.CharField(max_length=16)
    memsize = models.CharField(max_length=32)
    osname = models.CharField(max_length=16)
