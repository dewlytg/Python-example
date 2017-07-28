#coding:utf-8

"""
普通函数和lambda函数
"""
#无参数函数定义
def myfun1():
    print "My function"

##一般参数函数定义
def myfun2(x,y):
    print x + y

##默认参数函数定义
def myfun3(x,y,z="default"):
    print x + y + z

##args可变参数和kwargs关键字参数函数定义
def myfun4(x,y,*args,**kwargs):
    print x + y
    print args
    print kwargs

myfun1()
myfun2(1,2)
myfun3("a","b")
myfun4("a","b",1,2,3,name="James",age=23)

lam1 = lambda x,y:x+y
lam2 = lambda x:x % 2
print lam1(2,3)
print lam2(10)
