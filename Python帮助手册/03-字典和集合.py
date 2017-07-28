#coding:utf-8

"""
dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度
set和dict类似，也是一组key的集合，但不存储value，由于key不能重复，所以，在set中，没有重复的key
"""
#1)dict：
dic1 = {"name":"James","age":30,"sex":"male","salary":"1000000"}
dic2 = dict(name="Wade",age=32,sex="male",salary="1000000")
dic3 = {}.fromkeys(["name"],"Yao")

##查
print "name" in dic1
print dic1.has_key("name")
print dic1["name"]
print dic1.get("name")
print dic1.get("email","default@NBA.COM")
print dic1.keys()
print dic1.values()
print dic1.items()

#改和增
dic1["name"] = "JAMES"
dic1["email"] = "james@NBA.COM"
print dic1

#删
dic1.pop("name")
del dic1["age"]
dic1.clear()
print dic1

#2)set：
s1 = set([1,2,3])
s2 = set([2,3,4])
s3 = set([1,1,2,3,4])
print s1,s2,s3
s1.add(4)
print s1
s1.remove(4)
print s1
print s1 & s2
print s1 | s2