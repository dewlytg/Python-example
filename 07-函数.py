#coding:utf-8

"""
普通函数和lambda函数，print和return，print是当前终端显示结果，而return则是保留结果到一个对象中，如果没有return值，默认是None
理解函数即变量
"""
#无参数函数定义
def myfun1():
    print "My function"

##一般参数函数定义
def myfun2(x,y):
    print x + y
    return "general"

##默认参数函数定义
def myfun3(x,y,z="default"):
    print x + y + z
    return "default"

##args可变参数和kwargs关键字参数函数定义
def myfun4(x,y,*args,**kwargs):
    print x + y
    print args
    print kwargs
    return "variable and kewords"

ret1 = myfun1()
ret2 = myfun2(1,2)
ret3 = myfun3("a","b")
ret4 = myfun4("a","b",1,2,3,name="James",age=23)
print
print ret1,ret2,ret3,ret4

lam1 = lambda x,y:x+y
lam2 = lambda x:x % 2
print lam1(2,3)
print lam2(10)

##递归函数
def calc(n):
    print(n)
    if int(n/2) > 0:
        return calc(int(n/2))
    print("-->",n)

calc(10)
