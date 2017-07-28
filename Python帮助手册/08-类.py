#coding:utf-8

"""
class encapsulation, polymorphism, inheritance
"""
#1)类的详解:
class Student(object):
    """
    define a class for student
    """
    ##类和对象都可以调用,私有属性和方法只能内部调用,定义私有属性和方法"_"或者"__",__slot__限制用户自定义属性
    __slots__ = ("name","score","instance_attr","_instance_private","__instance_private","email")
    class_attr = "类属性"
    _class_private = "_ 私有类属性"
    __class_private = "__ 私有类属性"

    ##构造函数
    def __init__(self,name,score):
        ##只有对象可以调用
        self.instance_attr = "实例属性"
        self._instance_private = "_ 实例私有属性"
        self.__instance_private = "__ 实例私有属性"
        self.name = name
        self.score = score

    def print_score(self):
        print "%s: %s" %(self.name,self.score)
        self._privatemethod()
        self.__privatemethod()

    @property
    def get_propertymethod(self):
        # 静态方法可以访问类属性和实例属性
        print "属性方法"
        print Student.class_attr
        print Student._class_private
        print Student.__class_private
        print self.instance_attr
        print self._instance_private
        print self.__instance_private

    @staticmethod
    def get_staticmethod():
        # 静态方法可以访问类属性，不能访问实例属性
        print "静态方法"
        print Student.class_attr
        print Student._class_private
        print Student.__class_private

    @classmethod
    def get_classmethod(cls):
        ##类方法可以访问类属性，不能访问实例属性
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
stu01.print_score()

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
def set_score(self, email):
    self.email = email

Student.set_score = MethodType(set_score, None, Student)
stu02 = Student("james",23)
stu02.set_score("james@NBA.COM")
print
print stu02.email

print
print Student.__doc__
print stu01.__class__
print stu02.__class__.__bases__
print stu01

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