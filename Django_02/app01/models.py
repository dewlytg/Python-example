from django.db import models

# Create your models here.
class UserGroup(models.Model):
    # 自增 必须primary_kye = True
    uid = models.AutoField(primary_key=True)
    caption = models.CharField(max_length=32)
    ctime = models.DateTimeField(auto_now_add=True,null=True) #添加数据的时候自动生成时间,creattime
    utime = models.DateTimeField(auto_now=True,null=True) #修改数据的时候自动修改时间,updatetime

class UserInfo(models.Model):
    # 系统会自动生成一个id列，并且是primary_key
    # 创建用户名和密码两列，并且定义最大长度
    # 字符串 数字 时间 二进制 自增
    # verbose_name 也是在django admin中使用，显示中文名，blank 也是在django admin中使用，是否可以为空
    username = models.CharField(max_length=32,verbose_name="用户名",blank=True)
    password = models.CharField(max_length=64)
    # 下面EmailFiled DateTimeField GenericIPAddressField 都是在django admin中添加记录的时候有提示
    email = models.EmailField(max_length=32,null=True)
    # date_time = models.DateTimeField(max_length=32,null=True)
    # help_text也是在django admin中使用，可以看到下方的提示
    # ip = models.GenericIPAddressField(max_length=32,null=True,help_text="ip地址")
    # ForeignKey 外键，to_field 指定字段，userinfo对象中会多一个user_group_id字段，obj.user_group其实是一个UserGroup对象
    user_group = models.ForeignKey("UserGroup",to_field="uid",on_delete=True)

    user_type_choice = (
        (1,"管理员"),
        (2,"普通用户")
    )

    # choice也是在django admin中使用，可以看到下拉列表中有"管理员" 和 "普通用户" 选项
    user_type_id = models.IntegerField(choices=user_type_choice,null=True)
