#!/usr/bin/env python

import datetime,os,sys
from utils.handler import ShopFileHandler

fileobj = ShopFileHandler("./db/shop_userinfo")
user_info = fileobj.userinfo

def login(func,attempt_max=3,lock_time=60):
    def inner(*args,**kwargs):
        flag = True
        while flag:
            username = input("请输入您的用户名？".rjust(20, ">"))
            current_time = str(datetime.datetime.now())
            if username in user_info:
                if user_info[username]["is_locked"] == "True" and user_info[username]["lock_time"] > current_time:
                    print("对不起，你的用户还在锁定张，没有解锁")
                    flag = False
                else:
                    for i in range(attempt_max):
                        password = input("请输入您的密码？".rjust (20, ">"))
                        if user_info[username]["password"] == password:
                            is_successful = True
                            flag = False
                            kwargs["username"] = username
                            break
                        else:
                            print("密码错误，请重新输入")
                    else:
                        print("你已经尝试三次，用户锁定，请一小时后登录")
                        now_time = datetime.datetime.now()
                        expire_time = datetime.timedelta(minutes=lock_time) + now_time
                        user_info[username]["is_locked"] = "True"
                        user_info[username]["lock_time"] = str(expire_time)
                        fileobj.save2file()
                        flag = False
            else:
                print("对不起，你输入的用户名不存在，请重新输入")
        if is_successful:func(*args,**kwargs)
    return inner