#!/usr/bin/env python

import os,sys,json
from utils.handler import CreditCarHandler
from utils.handler import ShoppingHandler
from credit_auth import login
from utils.Logging import logger

sh_handler = ShoppingHandler("./db/shoplist")
sh_dict = sh_handler.get_shop_name_price_dict

msg = """
 欢迎登陆招商银行APP
    0) 基本信息
    1) 用户消费
    2) 用户还款
    3) 用户转账
    4) 用户取现
    5）购物车结算
"""

class CreditCar(object):
    @login
    def __init__(self,username=None):
        self.username = username
        if self.username == "anonumous":
            pass
        else:
            self.credit_card_file = os.path.join("./user_credit_card",self.username)
            self.user_obj = CreditCarHandler(self.credit_card_file)
            self.user_shop_car_file = os.path.join("./user_shop_car", self.username)
            self.user_shop_car_dict = json.load(open(self.user_shop_car_file))

    def userinfo(self):
        if self.username == "anonumous":
            print("只能看到基本页面")
        else:
            print(self.user_obj.data)

    def consume(self,money):
        if self.username == "anonumous":
            print("只能看到消费页面")
        else:
            self.user_obj.subtraction(money)
            self.user_obj.save()
            logger("info", "[%s] 消费了： [%s]" %(self.username,money) , self.username)

    def repay(self,money):
        if self.username == "anonumous":
            print("只能看到还款页面")
        else:
            self.user_obj.plus(money)
            self.user_obj.save()
            logger("info", "[%s] 还款： [%s]" % (self.username, money), self.username)

    def transfer(self,recipient,money):
        if self.username == "anonumous":
            print("只能查看到转钱页面")
        else:
            recipient_credit_card_file = os.path.join("./user_credit_card",recipient)
            recipient_obj = CreditCarHandler(recipient_credit_card_file)
            self.user_obj.subtraction(money)
            recipient_obj.plus(money)
            self.user_obj.save()
            recipient_obj.save()
            logger("info", "[%s] 收到 [%s] 的转账 [%s]" % (recipient,self.username,money), recipient)
            logger("info", "[%s] 转给 [%s] 金额是 [%s]" % (self.username,recipient,money), self.username)

    def withdraw(self,money):
        if self.username == "anonumous":
            print("只能查看到提现页面")
        else:
            amount = money + money * 0.05
            self.user_obj.subtraction(amount)
            if self.user_obj.data.get("cash"):
                self.user_obj.data["cash"] += money
            else:
                self.user_obj.data["cash"] = money
            self.user_obj.save()
            logger("info", "[%s] 提现的金额是： [%s]" % (self.username, money), self.username)

    def shopping_paid(self):
        print(self.user_shop_car_dict)
        option = input("请输入你想结算的商品名称和数量，用逗号分开")
        brand_name,brand_number = option.split(",")
        brand_price = sh_dict[brand_name]
        self.consume(int(brand_price) * int(brand_number))
        self.user_shop_car_dict["not_paid"][brand_name] = int(self.user_shop_car_dict["not_paid"][brand_name]) - int(brand_number)
        print(self.user_shop_car_dict["not_paid"][brand_name])
        fd = open(self.user_shop_car_file,"w")
        json.dump(self.user_shop_car_dict,fd)
        fd.close()

if __name__ == "__main__":
    print(msg)
    print("请先登陆招商生活APP".center(50,"*"))
    obj = CreditCar()
    while True:
        select_option = input("请选择编号，退出请按[q]，帮助请按[h]")
        if select_option == "q":
            break
        elif select_option == "h":
            print(msg)
        elif select_option == "0":
            obj.userinfo()
        elif select_option == "1":
            money = input("请输入消费金额")
            obj.consume(int(money))
        elif select_option == "2":
            money = input("请输入还款金额")
            obj.repay(int(money))
        elif select_option == "3":
            recipient = input("请输入转账给谁")
            money = input("请输入转账金额")
            obj.transfer(recipient,int(money))
        elif select_option == "4":
            money = input("请输入提现金额")
            obj.withdraw(int(money))
        elif select_option == "5":
            obj.shopping_paid()
        else:
            print("对不起，你选择的编号不对，请重新输入！")



