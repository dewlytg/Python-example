from django.db import models

# Create your models here.
class Business(models.Model):
    capition = models.CharField(max_length=32)
    code = models.CharField(max_length=32)

class Host(models.Model):
    nid = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=32,db_index=True)
    ip = models.CharField(max_length=32,db_index=True)
    port = models.IntegerField()
    b = models.ForeignKey("Business",to_field="id",on_delete=True)

class Application(models.Model):
    name = models.CharField(max_length=32,unique=True)
    r = models.ManyToManyField("Host")
