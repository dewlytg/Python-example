#coding:utf-8

"""
class encapsulation, polymorphism, inheritance
"""
#1)类的详解:
class Student(object):
    """
    define a class for student
    """
    ##类属性,类和对象都可以调用,私有属性和方法只能内部调用,定义私有属性和方法"_"或者"__",__slot__限制用户自定义属性
    __slots__ = ("name","score","instance_attr","_instance_private","__instance_private","email")
    class_attr = "类属性"
    _class_private = "_ 私有类属性"
    __class_private = "__ 私有类属性"

    ##构造函数
    def __init__(self,name,score):
        ##实例属性,只有对象可以调用
        self.instance_attr = "实例属性"
        self._instance_private = "_ 实例私有属性"
        self.__instance_private = "__ 实例私有属性"
        self.name = name
        self.score = score

    def get_hello(self):
        print "hello world!"

    def get_method(self):
        # 普通方法没有限制
        print "普通方法"
        print Student.class_attr
        print Student._class_private
        print Student.__class_private
        print self.instance_attr
        print self._instance_private
        print self.__instance_private
        self._privatemethod()
        self.__privatemethod()
        self.get_hello()

    @property
    def get_propertymethod(self):
        # 属性方法也没有限制，只是在调用方法的时候不用带'()'
        print "属性方法"
        print Student.class_attr
        print Student._class_private
        print Student.__class_private
        print self.instance_attr
        print self._instance_private
        print self.__instance_private
        self._privatemethod()
        self.__privatemethod()
        self.get_hello()

    @staticmethod
    def get_staticmethod():
        # 静态方法就是不用带self参数，静态方法可以访问类属性，不能访问实例属性，不能调用方法
        print "静态方法"
        print Student.class_attr
        print Student._class_private
        print Student.__class_private

    @classmethod
    def get_classmethod(cls):
        ## 类方法就是把self参数变成了cls，类方法可以访问类属性，不能访问实例属性，不能调用方法
        print "类方法"
        print cls.class_attr
        print cls._class_private
        print cls.__class_private

    def _privatemethod(self):
        print "_ 私有方法"

    def __privatemethod(self):
        print "__ 私有方法"

    ##在"print 实例名"的时候更直观，如果不定义会显示成<__main__.Student object at 0x0259B5A0>
    def __str__(self):
        return "%s is a Student instance" % self.name

    ##析构函数,删除一些数据，回收一些内存等
    def __del__(self):
        print "delete all datas"

stu01 = Student("tom",100)
stu01.get_method()

print
print stu01.class_attr
print stu01.instance_attr
print Student.class_attr

print
stu01.get_staticmethod()
stu01.get_classmethod()
stu01.get_propertymethod

##外部定义类方法
from types import MethodType
def set_email(self, email):
    self.email = email

Student.set_email = MethodType(set_email, None, Student)
stu02 = Student("james",23)
stu02.set_email("james@NBA.COM")
print
print stu02.email

print
print Student.__doc__
print stu01.__class__
print stu02.__class__.__bases__
print stu01
#############################################################################################
#__metaclass__ 和 __new__
#__new__是用来创建实例的特殊方法
class MyType(type):
    def __init__(self,what,bases=None,dict=None):
        print "---MyType init---"
        super(MyType,self).__init__(what,bases,dict)

    def __call__(self, *args, **kwargs):
        print "---MyType call---"
        obj = self.__new__(self,*args,**kwargs)
        self.__init__(obj,*args,**kwargs)

class Foo(object):
    __metaclass__ = MyType

    def __init__(self,name):
        self.name = name
        print "Foo ---init---"

    def __new__(cls, *args, **kwargs):
        print "Foo ---new---"
        return object.__new__(cls)

obj = Foo("dewly")
#print obj.name
#############################################################################################
#属性方法传值
class Dog(object):
    def __init__(self,name):
        self.name = name
        self.__food = None

    @property
    def eat(self):
        print "%s eat... %s" %(self.name,self.__food)

    @eat.setter
    def eat(self,food):
        print "%s eat %s" %(self.name,food)
        self.__food = food

    @eat.deleter
    def eat(self):
        del self.__food
        print "delete __food"

d = Dog("small")
d.eat #执行属性方法
d.eat = "骨头" #执行eat.setter
d.eat #执行属性方法
del d.eat #执行eat.deleter
#d.eat
############################################################################################
#通过type定义类
def __init__(self,name,age):
    self.name = name
    self.age = age

def func(self):
    print "Define a new class by type"
    print "hello,%s" % self.name

Foo = type("Foo",(object,),{"__init__":__init__,"talk":func})
f = Foo("james",22)
f.talk()
#############################################################################################
#反射，通过字符串调用类的属性调用
"""
hasattr: 根据提供的字符串判断对象是否有相应的属性，此属性可以是变量也可以是方法
getattr: 根据提供的字符串获取指定对象的属性，如果是变量则返回变量值，如果是方法则放回方法对象的内存地址
setattr: 根据提供的字符串定义一个新的属性，如果属性存在就覆盖原有属性
delattr: 根据提供的字符串删除指定属性
"""
def talk(self):
    print "%s is talking...."%self.name

class Dog(object):
    def __init__(self,name):
        self.name = name

    def bark(self):
        print "%s is barking..."%self.name

d = Dog("duoduo")
print hasattr(d,"name")
print hasattr(d,"bark")
print hasattr(d,"talk")
result = getattr(d,"name")
func = getattr(d,"bark")
print result
func()
setattr(d,"talk",talk)
d.talk(d)
delattr(d,"name")
print d.name


#############################################################################################
#2)继承:
class BaseClass:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def speak(self,name):
        print "base class is speak:%s" %name

class SubClass(BaseClass):
    def __init__(self,name,age,salary):
        BaseClass.__init__(self,name,age)
        self.salary = salary

    def talk(self,sth):
        print "%s talking %s" %(self.name,sth)
        BaseClass.speak(self,sth)

    ##此处有在子类中定义了speak方法，多态
    def speak(self,sth):
        print "sub class is spaak:%s" %sth

if __name__ == "__main__":
    s = SubClass("Joan",1,800)
    s.talk("a story")
    s.speak("b story")
    issubclass(SubClass,BaseClass)
    hasattr(s,"talk")

#############################################################################################
#类接口技术
"""
Super           定义一个method函数已经在子类中期待一个动作的delegate
Inheritor       没有提供任何新的变量名，因此会获得Super定义的一切内容
Replacer        用自己的版本覆盖Super的method
Extender        覆盖并回调默认method，从而定制Super的method
Provider        实现Super的delegate方法预期的action方法
"""
class Super:
    def method(self):
        print "in Super.method"
    def delegate(self):
        self.action()

class Inheritor(Super):
    pass

class Replacer(Super):
    def method(self):
        print "In Replacer.method"

class Extender(Super):
    def method(self):
        print "starting Extender.method"
        Super.method(self)
        print "ending Extender.method"

class Provider(Super):
    def action(self):
        print "in Provider.action"

if __name__ == "__main__":
    for klass in (Inheritor,Replacer,Extender):
        print "\n" + klass.__name__ + "..."
        klass().method()
    print "\nProvider..."
    x = Provider()
    x.delegate()

#############################################################################################
#assert,abstract
class Super:
    def delegate(self):
        self.action()

    def action(self):
        assert False,"action must be defined"

X = Super()
X.delegate()

from abc import ABCMeta,abstractmethod
class Super:
    __metaclass__ = ABCMeta
    def delegate(self):
        self.action()

    @abstractmethod
    def action(self):
        pass

class Sub(Super):pass

X = Sub()
