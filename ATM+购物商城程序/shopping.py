#!/usr/bin/env python

import os,json
from utils.handler import ShoppingHandler
from shop_auth import login

sh_handler = ShoppingHandler("./db/shoplist")
sh_list = sh_handler.data
cheapest_shop_price = sh_handler.cheapest_shop_price
print(sh_list)

@login
def trade(*args,**kwargs):
    username = kwargs["username"]
    user_shop_car_file = os.path.join("./user_shop_car",username)
    credit_card_file = os.path.join("./user_credit_card",username)
    credit_card_dict = json.load(open(credit_card_file))
    user_amount = int(credit_card_dict[username]["amount"])
    print(user_amount)
    if os.path.exists(user_shop_car_file):
        user_shop_car_dict = json.load(open(user_shop_car_file))
        print(user_shop_car_dict)
    else:
        user_shop_car_dict = {}
        user_shop_car_dict["is_paid"] = {}
        user_shop_car_dict["not_paid"] = {}
    while True:
        sh_handler.get_shop_list
        option = input("请输入你想购买的商品编号，退出按[q]")
        if option == "q":
            fd = open(user_shop_car_file, "w")
            json.dump(user_shop_car_dict,fd)
            fd.close()
            break
        else:
            shop_name = sh_list[int(option)]["name"]
            shop_price = int(sh_list[int(option)]["price"])
            if user_amount < cheapest_shop_price:
                print("你的钱已经不够购买最便宜的商品了！")
            else:
                if user_amount > shop_price:
                    if user_shop_car_dict["not_paid"].get(shop_name):
                        user_shop_car_dict["not_paid"][shop_name] += 1
                    else:
                        user_shop_car_dict["not_paid"][shop_name] = 1
                else:
                    print("你的钱已经不够购买此商品！")

if __name__ == "__main__":
    trade()