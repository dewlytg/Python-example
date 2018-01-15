#!/usr/bin/env python

import json,os

class ShopFileHandler(object):
    def __init__(self,filename):
        self.filename = filename
        self.data = json.load(open(self.filename))

    def __getitem__(self, item):
        return self.data[item]

    def __setitem__(self, key, value,is_locked=False):
        self.data[key] = {"password":value,"is_locked":is_locked}

    def __delitem__(self, key):
        del self.data[key]

    @property
    def userinfo(self):
        return self.data

    def save2file(self):
        fd = open(self.filename,"w")
        json.dump(self.data,fd)
        fd.close()

class CreditFileHandler(object):
    def __init__(self,filename):
        self.filename = filename
        self.data = json.load(open(self.filename))

    def __getitem__(self, item):
        return self.data[item]

    def __setitem__(self, key, value,amount=10000):
        self.data[key] = {"password":value,"amount":amount}

    def __delitem__(self, key):
        del self.data[key]

    @property
    def creditinfo(self):
        return self.data

    def save2file(self):
        fd = open(self.filename,"w")
        json.dump(self.data,fd)
        fd.close()

class ShoppingHandler(object):
    def __init__(self,filename):
        self.filename = filename
        self.data = json.load(open(self.filename))

    @property
    def get_shop_list(self):
        for index,value in enumerate(self.data):
            print("%s) 商品名称[%s] 商品价格 [%s]" %(index,value["name"],value["price"]))

    @property
    def get_shop_name_price_dict(self):
        result = {}
        for i in self.data:
            result[i["name"]] = int(i["price"])
        return result

    @property
    def cheapest_shop_price(self):
        price_list = []
        for i in self.data:
            price_list.append(int(i["price"]))
        return min(price_list)

class CreditCarHandler(object):
    def __init__(self,filename):
        self.filename = filename
        self.username = os.path.basename(self.filename)
        self.data = json.load(open(self.filename))

    def plus(self,money):
        self.data[self.username]["amount"] += int(money)

    def subtraction(self,money):
        self.data[self.username]["amount"] -= int(money)

    def save(self):
        fd = open(self.filename,"w")
        json.dump(self.data,fd)
        fd.close()

if __name__ == "__main__":
    pass