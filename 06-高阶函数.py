#coding:utf-8

"""
map,reduce,zip,filter,sorted,partical
"""

#1)map:
###map(function,iterable) function为函数，iterable是一个可迭代对象，返回值为列表类型
S1 = "abc"
S2 = "xyz123"

def f(x):
    return x * x

print map(f,[1,2,3,4,5,6,7,8,9])
print map(lambda x:x*x,[1,2,3,4,5,6,7,8,9])
print map(str,[1,2,3,4,5,6,7,8,9])
print map(str,[i for i in range(10)])
print map(int,"123")
print map(None,S1,S2)

#2)reduce:
###reduce(function,iterable)  function为函数，iterable是一个可迭代对象

def add(x,y):
    return x + y

print reduce(add,[1,2,3,4,5,6,7,8,9])

#3)zip:
print zip(["name","age"],["James",23])
print list(zip(S1,S2))

#4)filter:
###filter(function,iterable) function为函数，iterable是一个可迭代对象，返回值为列表类型
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def fun1(num):
    if num % 2 == 0:
        return True
    else:
        return False
l2  = filter(fun1,l1)
print l2

l2 = filter(lambda x:not x%2,l1)
print l2

#5)sorted:
###sorted(iterable,cmp=None,key=None,reverse=False)
"""
1.cmp，比较的函数，这个具有两个参数，参数的值都是从可迭代对象中取出，此函数必须遵守的规则为，大于则返回1，小于则返回-1，等于则返回0
2.key，主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序
3.reverse，是否反转，默认情况下不反转
"""
def cmp_value(x,y):
    if x > y :
        return 1
    elif x < y:
        return -1
    else:
        return 0
so = sorted('this is a string'.split(' '),cmp=cmp_value)
print so

import os
def sorted_ls(path):
    mtime = lambda f:os.stat(os.path.join(path, f)).st_mtime
    #return list(sorted(os.listdir(path),key=mtime,reverse=True))
    return list(sorted(os.listdir(path), key=mtime))

print(sorted_ls('.'))

#6)partial:
from operator import add, mul
from functools import partial

add10 = partial(add, 10)
print add10(20)
mul3 = partial(mul, 3)
print mul3(22)