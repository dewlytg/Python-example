#!/usr/bin/env python

import os,sys,json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from cfg import config

USER_HOME_DIR = config.USER_HOME_DIR
USER_ACCOUNT_DIR = config.USER_ACCOUNT_DIR

def user():
    username = input("请输入你的用户名？").strip ()
    user_account_file = os.path.join(USER_ACCOUNT_DIR, username)
    if not os.path.isfile(user_account_file):
        while True:
            password = input("请输入你的密码？").strip()
            password_2 = input("请再次输入密码？").strip()
            if password == password_2:
                f = open(user_account_file,"w")
                json.dump({"username":username,"password":password},f)
                f.close()
                break
            else:
                print("你输入的密码不一致，请重新输入")
    else:
        print("此用户已经存在！")

if __name__ == "__main__":
    user()