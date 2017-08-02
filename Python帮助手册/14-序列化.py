#coding:utf-8

"""
json 和 pickle
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