#coding:utf-8

"""
Python __func__ 魔术方法
"""

##基本定制
"""
C.__init__(self[, arg1, ...])         构造器（带一些可选的参数）
C.__new__(cls[, arg1, ...])           构造器（带一些可选的参数）;通常用在设置不变数据类型的子类
C.__del__(self)                       析构器,通常释放内存的操作放在这里
C.__str__(self)                       可打印的字符输出；内建str()及print语句
C.__repr__(self)                      运行时的字符串输出；内建repr()  ''和操作符
C.__unicode__(self)                   Unicode 字符串输出；内建unicode()
C.__call__(self, *args)               表示可调用的实例
C.__nonzero__(self)                   为object 定义False 值;内建bool() （从2.2 版开始）
C.__len__(self)                       长度（可用于类）;内建len()
"""
class A:
    def __init__(self):
        print "call __init__"

    def __str__(self):
        print "call __str__"
        return "class A str"

    def __repr__(self):
        print "call __repr__"
        return "class A repr"

    def __nozero__(self):
        print "call __nozero__"
        return 1

    def __len__(self):
        print "call __len__"
        return 1

    def __unicode__(self):
        print "call __unicode__"
        return "class A unicode"

    def __call__(self, *args, **kwargs):
        print "call __call__"
        return "calss A callale"

    def __del__(self):
        print "calll __del__"


a = A()
print a
print str(a)
print repr(a)
print len(a)
print bool(a)
print callable(a)

"""
__new__：创建对象时调用，返回当前对象的一个实例,相当于Java里面的构造器 一般是用于继承内置类的，返回值是一个对象
使用：需要控制一个新实例的创建,一般情况下不会使用，除非需要子类化不可变类型例如str/int/unicode/tuple

__init__：创建完对象后调用，对当前对象的实例的一些初始化，无返回值
使用：需要控制一个实例的初始化

可以这样理解，默认是创建（new），然后调用init(new的时候，self还不存在, init的时候self已经存在了)
"""
class B(object):
    def __init__(self):
        print "call __init__"
        self.value = 1

    def __new__(cls):
        print "call __new__"
        return super(B, cls).__new__(cls)

b = B()
print b.value

##对象值比较
"""
C.__cmp__(self, obj)                   对象比较；内建cmp()
C.__lt__(self, obj)                    and 小于/小于或等于；对应<及<=操作符
C.__le__(self,obj)
C.__gt__(self, obj)                    and 大于/大于或等于；对应>及>=操作符
C.__ge__(self,obj)
C.__eq__(self, obj)                    and 等于/不等于；对应==,!=及<>操作符
C.__ne__(self,obj)
"""
class C:
    def __init__(self,value):
        self.value = value

    def __cmp__(self, other):
        print "call __cmp__"
        return self.value - other.value

    def __lt__(self, other):
        print "call __lt__"
        return self.value < other.value

    def __gt__(self, other):
        print "call __gt__"
        return self.value > other.value

    def __eq__(self, other):
        print "call __eq__"
        return self.value == other.value

c1 = C(1)
c2 = C(2)
print cmp(c1,c2)
print c1 < c2
print c1 > c2
print c1 == c2

##属性操作
"""
C.__getattr__(self, attr)           获取属性；内建getattr()；仅当属性没有找到时调用
C.__setattr__(self, attr, val)      设置属性
C.__delattr__(self, attr)           删除属性
C.__getattribute__(self, attr)      获取属性；内建getattr()；总是被调用
C.__get__(self, attr) （描述符）     获取属性
C.__set__(self, attr, val)         （描述符）设置属性
C.__delete__(self, attr)           （描述符）删除属性
"""

class D:
    def __init__(self):
        self.value = 1

    def __getattr__(self, key):
        print "call __getattr__"
        try:
            return self.__dict__[key]
        except:
            return "not found"

    def __setattr__(self, key, value):
        print "call __setattr__"
        self.__dict__[key] = value

    def __delattr__(self, key):
        print "call __delattr__"
        del self.__dict__[key]

    def __getattribute__(self, key):
        print "call __getattribute__"
        return self.__dict__[key]

d = D()
d.name = "James"
d.age = 23
print d.name,d.age
del d.name
del d.age

##序列
"""
C.__len__(self)              序列中项的数目
C.__getitem__(self, ind)     得到单个序列元素
C.__setitem__(self, ind,val) 设置单个序列元素
C.__delitem__(self, ind)     删除单个序列元素

C.__getslice__(self, ind1,ind2)    得到序列片断
C.__setslice__(self, i1, i2,val)   设置序列片断
C.__delslice__(self, ind1,ind2)    删除序列片断
C.__contains__(self, val) f        测试序列成员；内建in 关键字
C.__*add__(self,obj)               串连；+操作符
C.__*mul__(self,obj)               重复；*操作符
C.__iter__(self)                   创建迭代类；内建iter()
"""
class E:
    def __init__(self):
        print "call __init__"
        self.value = {}

    def __len__(self):
        print "call __len__"
        return len(self.value)

    def __getitem__(self, key):
        print "call __getitem__"
        return self.value[key]

    def __setitem__(self, key, value):
        print "call __setitem__"
        self.value[key] = value

    def __delitem__(self, key):
        print "call __delitem__"
        del self.value[key]

e = E()
print len(e)
e["name"] = "James"
print e["name"]
del e["name"]