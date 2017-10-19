#coding:utf-8

"""
json 和 pickle
json 支持所有语言通用
pickle只支持python语言
shelve
"""
import json,pickle

data = {"name":"James","age":"32"}
with open("data.json","w") as fd:
    json.dump(data,fd)

with open("data.json","r") as fd:
    data = json.load(fd)
    print data

shoplist = ["apple","mango","carrot"]
with open("data.pick","w") as fd:
    pickle.dump(shoplist,fd)

with open("data.pick","r") as fd:
    data = pickle.load(fd)
    print data


import datetime,shelve
d = shelve.open("shelve_test")

info = {"name":"james","age":33}
d["info"] = info
d["job"] = "nba"
d["date"] = datetime.datetime.now()
d.close()

print d.get("job")
print d.get("info")
print d.get("date")