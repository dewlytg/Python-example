#coding:utf-8

"""
在Python中，很多对象都是可以通过for语句来直接遍历的，例如list、string、dict等等，这些对象都可以被称为可迭代对象。至于说哪些对象是可以被迭代访问的，就要了解一下迭代器相关的知识了

迭代器
迭代器对象要求支持迭代器协议的对象，在Python中，支持迭代器协议就是实现对象的__iter__()和next()方法。其中__iter__()方法返回迭代器对象本身；next()方法返回容器的下一个元素，在结尾时引发StopIteration异常。

__iter__()和next()方法
这两个方法是迭代器最基本的方法，一个用来获得迭代器对象，一个用来获取容器中的下一个元素
对于可迭代对象，可以使用内建函数iter()来获取它的迭代器对象：

"""
li = [1,2]
it = iter(li)
print it
print it.next()
print it.next()
#print it.next()


"""
下面例子中实现了一个MyRange的类型，这个类型中实现了__iter__()方法，通过这个方法返回对象本身作为迭代器对象；同时，实现了next()方法用来获取容器中的下一个元素，当没有可访问元素后，就抛出StopIteration异常
"""
class MyRange(object):
    def __init__(self,n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def next(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()

myRange = MyRange(3)
for i in myRange:
    print i

"""
迭代器和可迭代对象
在上面的例子中，myRange这个对象就是一个可迭代对象，同时它本身也是一个迭代器对象。
看下面的代码，对于一个可迭代对象，如果它本身又是一个迭代器对象，就会有下面的问题，就没有办法支持多次迭代。
"""

print myRange
print iter(myRange)
print myRange is iter(myRange)
print [i for i in myRange]
print [i for i in myRange]


class Zrange:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return ZrangeIterator(self.n)

class ZrangeIterator:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def next(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration ()

zrange = Zrange(3)
print zrange
print iter(zrange)
print zrange is iter(zrange)

print [i for i in zrange]
print [i for i in zrange]

"""
生成器

在Python中，使用生成器可以很方便的支持迭代器协议。生成器通过生成器函数产生，生成器函数可以通过常规的def语句来定义，但是不用return返回，而是用yield一次返回一个结果，在每个结果之间挂起和继续它们的状态，来自动实现迭代议。
也就是说，yield是一个语法糖，内部实现支持了迭代器协议，同时yield内部是一个状态机，维护着挂起和继续的状态。
下面看看生成器的使用：
"""
def Zrange(n):
    i = 0
    while i < n:
        yield i
        i += 1

zrange = Zrange(3)
print zrange
print [i for i in zrange]

"""
生成器执行流程
下面就仔细看看生成器是怎么工作的。
从上面的例子也可以看到，生成器函数跟普通的函数是有很大差别的。
结合上面的例子我们加入一些打印信息，进一步看看生成器的执行流程：
"""

def Zrange(n):
    print "beginning of Zrange"
    i = 0
    while i < n:
        print "before yield",i
        yield i
        i += 1
        print "after yield",i
    print "endding of Zrange"

zrange = Zrange(3)
print "---------------"

print zrange.next()
print "---------------"

print zrange.next()
print "---------------"

print zrange.next()
print "---------------"

#print zrange.next()
#print "---------------"

"""
通过结果可以看到：
    当调用生成器函数的时候，函数只是返回了一个生成器对象，并没有 执行。
    当next()方法第一次被调用的时候，生成器函数才开始执行，执行到yield语句处停止next()方法的返回值就是yield语句处的参数（yielded value）
    当继续调用next()方法的时候，函数将接着上一次停止的yield语句处继续执行，并到下一个yield处停止；如果后面没有yield就抛出StopIteration异常
"""

##生成器表达式
gen = (i for i in range(50) if i%2)
print gen
print "__iter__" in dir(gen)
print "next" in dir(gen)
print sum(gen)

"""
生成器的send()和close()方法

生成器中还有两个很重要的方法：send()和close()。

send(value):
从前面了解到，next()方法可以恢复生成器状态并继续执行，其实send()是除next()外另一个恢复生成器的方法。
Python 2.5中，yield语句变成了yield表达式，也就是说yield可以有一个值，而这个值就是send()方法的参数，所以send(None)和next()是等效的。同样，next()和send()的返回值都是yield语句处的参数（yielded value）
关于send()方法需要注意的是：调用send传入非None值前，生成器必须处于挂起状态，否则将抛出异常。也就是说，第一次调用时，要使用next()语句或send(None)，因为没有yield语句来接收这个值。

close():
这个方法用于关闭生成器，对关闭的生成器后再次调用next或send将抛出StopIteration异常。
下面看看这两个方法的使用：
"""

def Zrange(n):
    i = 0
    while i < n:
        val = yield i
        print "val is :",val
        i += 1

zrange = Zrange(5)

print
print zrange.next()
print
print zrange.next()
print
print zrange.send("Hello")
zrange.close()
#print zrange.send("world")