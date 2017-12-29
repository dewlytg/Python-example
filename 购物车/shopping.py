#!/usr/bin/env python
#coding:utf-8
#author:TG

import json,sys,time,datetime,os

def auth_login(func):
    def inner(*args, **kwargs):
        with open("auth") as fd:user_dict = json.load(fd)
        print("-------------------------------->>>欢迎登录购物车页面<<<---------------------------------------")
        while True:
            u = input(">>>请输入你的用户名？")
            if user_dict.get(u, None):
                user_status_file = os.path.join("UserStatus",u)
                print(user_status_file)
                if os.path.exists(user_status_file):
                    with open(user_status_file) as fd:user_info = json.load(fd)
                    current_time = datetime.datetime.now()
                    if user_info.get("is_locked",None) and user_info.get("expire_time",None) > str(current_time):
                        print("账号已经锁定,还没有到时间.")
                        sys.exit()
                    elif user_info.get("is_locked",None) and user_info.get("expire_time",None) < str(current_time):
                        print("账号已经解锁,可以登录.")
                        del user_info["is_locked"]
                        del user_info["expire_time"]
                        with open(user_status_file,"w") as fd:json.dump(user_info,fd)
                for i in range(3):
                    is_login = False
                    p = input(">>>密码？")
                    if user_dict[u] == p:
                        print("#########登录成功#########")
                        is_login = True
                        break
                    else:
                        print("密码错误，请重新输入")
                        continue
                else:
                    print("用户锁定")
                    now_time = datetime.datetime.now()
                    expire_time = datetime.timedelta(minutes=60) + now_time
                    user_locked_dict = {"is_locked":True,"expire_time":str(expire_time)}
                    with open(user_status_file, "w") as fd:fd.write(json.dumps(user_locked_dict))
                    sys.exit()
                if is_login:
                    kwargs["username"] = u
                    return func(*args,**kwargs)
            else:
                print("此用户不存在")
    return inner

@auth_login
def show_shoppinglist(*args,**kwargs):
    with open("shoplist") as fd:shopping_list = json.load(fd)
    price_list = []
    username = kwargs["username"]
    user_status_file = os.path.join("UserStatus", username)
    if os.path.exists(user_status_file):
        with open (user_status_file) as fd:
            res = json.load(fd)
        if res.get("shopcar", None):
            pass
        else:
            res["shopcar"] = {}
        user_status_dic = res
    else:
        user_status_dic = {"shopcar": {}}
    while True:
        print("-------------------------------下面是商品列表-------------------------------")
        for i,row in enumerate(shopping_list):
            print(i,row["name"],row["price"])
            price_list.append(row["price"])
        print(user_status_dic)
        if user_status_dic.get("balance",None):
            money = user_status_dic["balance"]
        else:
            money = input ("------------------>输入你的工资：")
        select_option = input ("-------------------->选择你要购买的商品编号：")
        if select_option == "q":
            with open(user_status_file, "w") as fd:json.dump(user_status_dic, fd)
            sys.exit()
        else:
            if int(money) < min(price_list):
                print("你的资金不足")
                print(shopping_list[int(select_option)]["price"])
            elif int(money) > shopping_list[int(select_option)]["price"]:
                if user_status_dic.get("shopcar",None):
                    if user_status_dic["shopcar"].get(shopping_list[int(select_option)]["name"],None):
                        print(user_status_dic["shopcar"][shopping_list[int(select_option)]["name"]],"eeeeeeee")
                        user_status_dic["shopcar"][shopping_list[int(select_option)]["name"]] += 1
                    else:
                        user_status_dic["shopcar"][shopping_list[int(select_option)]["name"]] = 1
                else:
                    user_status_dic["shopcar"] = {}
                    user_status_dic["shopcar"][shopping_list[int(select_option)]["name"]] = 1
                user_status_dic["balance"] = int(money) - shopping_list[int (select_option)]["price"]
            else:
                print("你的资金不够买次商品")

if __name__ == "__main__":
    show_shoppinglist()
