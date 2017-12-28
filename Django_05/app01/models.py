from django.db import models

# Create your models here.
class User(models.Model):
    id  = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32,unique=True,db_index=True)
    pwd = models.CharField(max_length=64)
    email = models.CharField(max_length=64,unique=True,db_index=True)

class Host(models.Model):
    hostname = models.CharField(max_length=64,db_index=True)
    ip = models.GenericIPAddressField(db_index=True)
    port = models.IntegerField()
    g = models.ForeignKey("HostGroup",to_field="id",on_delete=True)

class HostGroup(models.Model):
    name = models.CharField(max_length=64)

class Applicaton(models.Model):
    name = models.CharField(max_length=64)
    h = models.ManyToManyField("Host")