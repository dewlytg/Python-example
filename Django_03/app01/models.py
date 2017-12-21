from django.db import models

# Create your models here.
class Business(models.Model):
    # auto create primary key from django
    caption = models.CharField(max_length=32)
    code = models.CharField(max_length=32)

class Host(models.Model):
    nid = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=32,db_index=True)
    ip = models.GenericIPAddressField(db_index=True)
    port = models.IntegerField()
    b = models.ForeignKey("Business",to_field="id",on_delete=True)

# 自定义多对多
# class Application(models.Model):
#     name = models.CharField(max_length=32)
#
# class HostToApp(models.Model):
#     hobj = models.ForeignKey("Host",to_field="nid",on_delete=True)
#     aobj = models.ForeignKey("Application",to_field="id",on_delete=True)

# 通过django orm 自动产生多对多
class Application(models.Model):
    name = models.CharField(max_length=32)
    r = models.ManyToManyField("Host")