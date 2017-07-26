#!/usr/bin/env python
# coding:utf-8

#############################################################################################
import MySQLdb

##MySQLdb模块使用,读取数据并且写入文件
class SelectMySQL(object):
    def __init__(self, host, port, user, passwd, db):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.db = db

    def select_data(self, sql):
        result = []
        conn = MySQLdb.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.db,
                               charset='utf8', )
        cur = conn.cursor()
        cur.execute(sql)
        alldata = cur.fetchall()
        for rec in alldata:
            result.append(rec)
        cur.close()
        conn.close()
        return result

    def get_result(self, sql, filename):
        results = self.select_data(sql)
        print('The amount of datas: %d' % (len(results)))
        with open(filename, 'w') as f:
            for result in results:
                f.write(str(result) + '\n')
        print('Data write is over!')
        return results


#############################################################################################
import urllib2


class BaiduMap(object):
    def baidu_api(self, lat, lng):
        url = 'http://api.map.baidu.com/geocoder/v2/'
        aklist = ['gGP0KevdCS7jBNus9CT9sUlepb1Kd9Of', '1UOzszXucpTPMEbtxv1Pe4QHoXrFGjUz']
        callback = 'renderReverse'
        location = lat + ',' + lng
        output = '&output=json&pois=1'
        url_path = url + '?ak=' + aklist[0] + '&callback' + callback + '&location=' + location + output
        result = urllib2.urlopen(url_path)
        hjson = json.loads(result.read())
        district = hjson['result']['addressComponent']['district']
        city = hjson['result']['addressComponent']['city']
        return district, city

    def get_result(self, infilename, outfilename):
        result_dict = {}
        with open(infilename, 'r') as f:
            for line in f.readlines():
                line = line.strip()
                lat = line.split(',')[0]
                lng = line.split(',')[1]
                district, city = self.baidu_map(lat, lng)
                if not result_dict.has_key(city):
                    result_dict[city] = {}
                else:
                    if result_dict[city].has_key(district):
                        result_dict[city][district] += 1
                    else:
                        result_dict[city][district] = 1
            with open(outfilename, 'w') as fp:
                json.dump(result_dict, fp)


#############################################################################################
class GoogleMap(object):
    def google_api(self, lat, lng):
        key = 'AIzaSyDqtufDx_z81iZ77V71_x1Y83ZVE1-XeKM'
        proxy_handler = urllib2.ProxyHandler({'http': 'ip:port'})
        opener = urllib2.build_opener(proxy_handler)
        ###url_path = "'https://maps.googleapis.com/maps/api/geocode/json?latlng=%s,%s&key=%s" % (lat,lng,key)
        url_path = "http://maps.googleapis.com/maps/api/geocode/json?latlng=%s,%s&language=zh_CN" % (lat, lng)
        result = opener.open(url_path).read().decode('utf-8')
        jret = json.loads(result)
        district = jret["results"][1]["address_components"][0]["long_name"]
        city = jret["results"][1]["address_components"][1]["long_name"]
        return district, city

    #############################################################################################


###json数据保存和读取
import json
import time

###Writing JSON data
data = {'name': 'james', 'age': '32'}
with open('data.json', 'w') as f:
    json.dump(data, f)

###Reading data back
with open('data.json', 'r') as f:
    data = json.load(f)

############################################################################################# 

###发送邮件

import smtplib, mimetypes
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.Header import Header
from email.mime.image import MIMEImage
import sys


def send_mail(_to_email, _subject, _message):
    _from_email = 'zabbix@cutt.com'
    msg = MIMEMultipart()
    msg['From'] = _from_email
    msg['To'] = _to_email
    msg['Subject'] = Header('zabbix-监控报警', charset='UTF-8')
    txt = MIMEText(_message, _subtype='plain', _charset='UTF-8')
    msg.attach(txt)
    smtp = smtplib.SMTP()
    smtp.connect('smtp.mxhichina.com:25')
    smtp.login('zabbix@example', '123')
    smtp.sendmail(_from_email, _to_email, msg.as_string())
    smtp.quit()


if __name__ == '__main__':
    send_mail(sys.argv[1], sys.argv[2], sys.argv[3])

############################################################################################# 

###glob文件名匹配
import glob

###获取指定目录下的所有图片
print glob.glob(r"E:/Picture/*.jpg")

#############################################################################################

###commands执行命令
import commands

###此函数是返回命令执行返回值以及执行结果
commands.getstatusoutput('cmd')

###此函数只返回结果,不返回返回值
commands.getoutput('cmd')

###此函数返回执行结果
commands.getstatus('cmd')
#############################################################################################

###os模块
import os

"""
os.sep:取代操作系统特定的路径分隔符
os.name:指示你正在使用的工作平台。比如对于Windows，它是'nt'，而对于Linux/Unix用户，它是'posix'。
os.getcwd:得到当前工作目录，即当前python脚本工作的目录路径。
os.getenv()和os.putenv:分别用来读取和设置环境变量
os.listdir():返回指定目录下的所有文件和目录名
os.remove(file):删除一个文件
os.stat（file）:获得文件属性
os.chmod(file):修改文件权限和时间戳
os.mkdir(name):创建目录
os.rmdir(name):删除目录
os.removedirs（r“c：\python”）:删除多个目录
os.system():运行shell命令
os.exit():终止当前进程
os.linesep:给出当前平台的行终止符。例如，Windows使用'\r\n'，Linux使用'\n'而Mac使用'\r'
os.path.split():返回一个路径的目录名和文件名
os.path.isfile()和os.path.isdir()分别检验给出的路径是一个目录还是文件
os.path.exists():检验给出的路径是否真的存在
os.curdir:返回当前目录（'.'）
os.chdir(dirname):改变工作目录到dirname
os.path.isdir(name):判断name是不是目录，不是目录就返回false
os.path.isfile(name):判断name这个文件是否存在，不存在返回false
os.path.exists(name):判断是否存在文件或目录name
os.path.getsize(name):或得文件大小，如果name是目录返回0L
os.path.abspath(name):获得绝对路径
os.path.isabs():判断是否为绝对路径
os.path.normpath(path):规范path字符串形式
os.path.splitext():分离文件名和扩展名
os.path.join(path,name):连接目录与文件名或目录
os.path.basename(path):返回文件名
os.path.dirname(path):返回文件路径
os.stat("file").st_size == 0 文件为空
"""

#############################################################################################

import optparse

# usage 定义的是使用方法，%prog 表示脚本本身，version定义的是脚本名字和版本号
parse = optparse.OptionParser(usage='"usage:%prog [options] arg1,arg2"', version="%prog 1.2")
parse.add_option('-u', '--user', dest='user', action='store', type=str, metavar='user', help='Enter User Name!!')
parse.add_option('-p', '--port', dest='port', type=int, metavar='port', default=3306, help='Enter Mysql Port!!')
parse.add_option('-v', help='Mysql Version!!')
# -u,--user 表示一个是短选项 一个是长选项
# dest='user' 将该用户输入的参数保存到变量user中，可以通过options.user方式来获取该值
# type=str，表示这个参数值的类型必须是str字符型，如果是其他类型那么将强制转换为str（可能会报错）
# metavar='user'，当用户查看帮助信息，如果metavar没有设值，那么显示的帮助信息的参数后面默认带上dest所定义的变量名
# help='Enter..',显示的帮助提示信息
# default=3306，表示如果参数后面没有跟值，那么将默认为变量default的值
parse.set_defaults(v=1.2)  # 也可以这样设置默认值
options, args = parse.parse_args()
print 'OPTIONS:', options
print 'ARGS:', args

print '~' * 20
print 'user:', options.user
print 'port:', options.port
print 'version:', options.v

#############################################################################################

###getopt参数模块
import getopt

"""
get_opt.py -a -b 5 --mm --directory /home
在上面的命令中sys.argv中存的分别是
['get_opt.py','-a','-b','5','--mm','--directory','/home'],
'-a'代表不需要附加参数的短选项
'-b'代表需要附加参数的短选项,同时5就是其附加参数
'--mm'代表不需要附加参数的长选项
'--directory'代表需要附加参数的长选项,同时/home就是其附加参数。
getopt函数的格式是getopt.getopt(命令行参数，"短选项",[长选项]）
其中如果短选项需要附加参数则在短选项后面加：，如果长选项需要添加参数则在长选项后添加=。返回值有两个，一个是对应的参数选项和value元组，另一个是除去有用参数外的其他命令行输出。
上面例子对应的格式为
getopt.getopt(sys.argv[1:],'ab:',['mm','directory='])
第一个返回值为[('-a', ''), ('-b', '5'), ('--mm', ''), ('--directory', '/home')] ，第二个返回值为空。
"""
#############################################################################################
"""
配置文件config.ini如下：

[user]
username = tom
password = ***
email = test@host.com

[book]
bookname = python
bookprice = 25
"""

###ConfigParser模块
import ConfigParser
import sys

###生成config对象
conf = ConfigParser.ConfigParser()

###用config对象读取配置文件
conf.read("config.ini")

###以列表形式返回所有的section
sections = conf.sections()
print 'sections:', sections  # sections: ['user', 'book']

###得到指定section的所有option
options = conf.options("user")
print 'options:', options  # options: ['username', 'password', 'email']

###得到指定section的所有键值对
useritem = conf.items("user")
print 'user:', useritem  # user: [('username', 'tom'), ('password', '***'), ('email', 'test@host.com')]

###指定section，option读取值
str_val = conf.get("book", "bookname")
int_val = conf.getint("book", "bookprice")

print "value for book's bookname:", str_val  # value for book's bookname: python
print "value for book's bookprice:", int_val  # value for book's bookprice: 25

###写配置文件
###更新指定section，option的值
conf.set("book", "bookname", "python learning")

###写入指定section增加新option和值
conf.set("book", "bookpress", u"人民邮电出版社")

###增加新的section
conf.add_section('purchasecar')
conf.set('purchasecar', 'count', '1')

###写回配置文件
conf.write(open("config.ini", "w"))

#############################################################################################

###try 异常处理
try:
    module = raw_input("请输入你想导入的模块？")
    __import__(module)
except Exception, e:
    print e
else:
    print "导入成功！"
finally:
    print "结束！"
#############################################################################################
###paramiko 模块使用
import paramiko

hostname = ""
username = ""
password = ""
port = ""


class SshClass():
    """
    This Class is a SSH for paramiko
    """

    def __init__(self, hostname, username, password, port):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.port = port

    def ssh_command(self, execcommand):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.hostname, port=self.port, username=self.username, password=self.password)
        stdin, stdout, stderr = ssh.exec_command(execcommand)
        ret = stdout.readlines()
        ssh.close()
        return ret

    def ssh_fileput(self, remote, local):
        t = paramiko.Transport((self.hostname, self.port))
        t.connect(username=self.username, password=self.password)
        sftp = paramiko.SFTPClient.from_transport(t)
        remotepath = remote
        localpath = local
        sftp.put(localpath, remotepath)
        t.close()

    def ssh_fileget(self, remote, local):
        t = paramiko.Transport((self.hostname, self.port))
        t.connect(username=self.username, password=self.password)
        sftp = paramiko.SFTPClient.from_transport(t)
        remotepath = remote
        localpath = local
        sftp.get(remotepath, localpath)
        t.close()


if __name__ == "__main__":
    s1 = SshClass(hostname, username, password, port)
#############################################################################################
###shutil模块

import shutil

shutil.rmtree("dir")  ###删除目录包括里面的文件内容
#############################################################################################
###gzip 模块

import gzip

f_in = open('file.txt', 'rb')
f_out = gzip.open('file.txt.gz', 'wb')
f_out.writelines(f_in)
f_out.close()
f_in.close()
#############################################################################################
###time 模块

###将字符串的时间转换为时间戳
import time

a = "2013-10-10 23:40:00"
timeArray = time.strptime(a, "%Y-%m-%d %H:%M:%S")
timeStamp = int(time.mktime(timeArray))

###时间戳转换为指定格式日期
timeStamp = 1381419600
timeArray = time.localtime(timeStamp)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)


def delta_time(starttime, endtime, today=None):
    stime = today + ' ' + starttime
    etime = today + ' ' + endtime
    stimeArray = time.strptime(stime, "%Y-%m-%d %H:%M:%S")
    etimeArray = time.strptime(etime, "%Y-%m-%d %H:%M:%S")
    stimeStamp = int(time.mktime(stimeArray))
    etimeStamp = int(time.mktime(etimeArray))
    delta = etimeStamp - stimeStamp
    return delta


#############################################################################################

from sys import argv

script, user_name = argv
prompt = '> '
print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)
print "Where do you live %s?" % user_name
lives = raw_input(prompt)
print "What kind of computer do you have?"
computer = raw_input(prompt)
print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)
#############################################################################################


##内建函数
__builtins__
##判断函数是否可以调用
callable(函数)
##随机数
import random

random.choice("students")

#############################################################################################
str(), repr(), format()  # 将非字符型数据转换为字符
int()  # 转换整数
float()  # 转换浮点数

list(s)  # 将字符s转为列表
tuple(s)  # 将字符s转为元组
set(s)  # 将字符s转为集合
frozenset(s)  # 将字符s转为不可变集合
dict(d)  # 创建字典，其d必须是(key,value)的元组序列

chr(x)  # 将整数转为字符
ord(x)  # 将字符转换为整数值
hex(x)  # 将整数转换为16进制字符
bin(x)  # 将整数转换为2进制字符
oct(x)  # 将整数转换为8进制字符
#############################################################################################
# 1  1  1  1 1 1 1 1
# 128 64 32 16 8 4 2 1

##都变成2进制预算
x << y  # x向左移动y位置
x >> y  # x向右移动y位置
x & y  # 按位与 255 & 101
x | y  # 按位或 255 | 101
x ^ y  # 按位异或 255 ^ 101
~x  # 按位求反
#############################################################################################
import copy

l1 = [1, 2, 3, 4, 5]
l2 = copy.deepcopy(l1)
print l1, l2
#############################################################################################
##根据mtime对文件排序
import os


def sorted_ls(path):
    mtime = lambda f: os.stat(os.path.join(path, f)).st_mtime
    return list(sorted(os.listdir(path), key=mtime))


print(sorted_ls('documents'))
#############################################################################################
##枚举
l1 = ['tg', 'zf']
for i, j in enumerate(l1):
    print i, j
#############################################################################################
##效果显示，sysout输入不换行直接输出，再次输出可以覆盖
import time, sys

counter = 0

sys.stdout.write('#' * 20)
sys.stdout.flush()

while True:
    sys.stdout.write("\r%sA" % ('#' * counter))
    sys.stdout.flush()
    counter += 1
    try:
        time.sleep(0.2)
    except KeyboardInterrupt:
        print "\nexit program."
        break
    if counter == 20:
        sys.stdout.write("\r" + '#' * 20)
        sys.stdout.flush()
        counter = 0
#############################################################################################
##字符串对齐
str.center(self, width)  ##居中对齐
str.ljust(self, width)  ##左对齐
str.rjust(self, width)  ##右对齐
#############################################################################################
##string模板
t = string.Template("my name is $name,password is $password")
t.substitute(name='tg', password='123456')
#############################################################################################
##pickle 存储器
import cPickle as p

shoplistfile = "shoplist.data"
shoplist = ["apple", "mango", "carrot"]

##写入文件
f = file(shoplistfile, 'w')
p.dump(shoplist, f)
f.close()

del shoplist

##读取数据
f = file(shoplistfile)
storedlist = p.load(f)
print storedlist
#############################################################################################
##raise 抛出异常
##使用raise抛出异常当程序出现错误，python会自动引发异常，也可以通过raise显示地引发异常。一旦执行了raise语句，raise后面的语句将不能执行
inputValue = raw_input("please input a int data :")
if type(inputValue) != type(1):
    raise ValueError
else:
    print inputValue

##assert 断言
"""
1.assert语句用来声明某个条件是真的。
2.如果你非常确信某个你使用的列表中至少有一个元素，而你想要检验这一点，并且在它非真的时候引发一个错误，那么assert语句是应用在这种情形下的理想语句。
3.当assert语句失败的时候，会引发一AssertionError。
	
>>> mylist = ['item']
>>> assert len(mylist) >= 1
>>> mylist.pop()
'item'
>>> assert len(mylist) >= 1
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
AssertionError
>>>
"""
#############################################################################################
##过滤一个列表，只提取奇数
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def fun1(num):
    if num % 2:
        return True
    else:
        return False


l2 = filter(fun1, l1)
print l2

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2 = filter(lambda num: num % 2, l1)
print l2

##对一个列表实现累加，使用reduce
l1 = [1, 2, 3, 4, 5]


def add(x, y):
    return x + y


result = reduce(add, l1)
print result

l1 = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, l1)
print result


#############################################################################################
##闭包
def line_conf():
    def line(x):
        return 2 * x + 1

    return line  # return a function object


my_line = line_conf()
print(my_line(5))
#############################################################################################
##偏函数
from operator import add, mul
from functools import partial

add10 = partial(add, 10)
add10(20)
mul3 = partial(mul, 3)
mul3(22)
#############################################################################################
###装饰器
import time


def deco(func):
    def timeit():
        print "prog start at:", time.ctime()
        newList = func()
        print "prog done at:", time.ctime()
        return newList

    return timeit


@deco
def loop2(n=10):
    time.sleep(1)
    myList = []
    for i in range(n):
        if i % 2:
            myList.append(i)
    return myList


print loop2()


#############################################################################################
###属性方法
class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


s = Student()
s.score = 60
print s.score
s.score = 100

#############################################################################################
###md5运算
##小文件md5
import hashlib

f = file("/etc/passwd")
data = f.read()
f.close()
m = hashlib.md5(data)
m.hexdigest()

##大文件md5,一次读外内存会溢出
m = hashlib.md5()
f = file('/etc/passwd')
while True:
    data = f.read(1024)
    if len(data) == 0:
        break
    m.update(data)
m.hexdigest()
#############################################################################################
###Python提供了__future__模块，把下一个新版本的特性导入到当前版本，于是我们就可以在当前版本中测试一些新版本的特性。举例说明如下：
###为了适应Python 3.x的新的字符串的表示方法，在2.7版本的代码中，可以通过unicode_literals来使用Python 3.x的新的语法：
# still running on Python 2.7
from __future__ import unicode_literals

print '\'xxx\' is unicode?', isinstance('xxx', unicode)
print 'u\'xxx\' is unicode?', isinstance(u'xxx', unicode)
print '\'xxx\' is str?', isinstance('xxx', str)
print 'b\'xxx\' is str?', isinstance(b'xxx', str)

###注意到上面的代码仍然在Python 2.7下运行，但结果显示去掉前缀u的'a string'仍是一个unicode，而加上前缀b的b'a string'才变成了str：
"""
$ python task.py
'xxx' is unicode? True
u'xxx' is unicode? True
'xxx' is str? False
b'xxx' is str? True
"""


#############################################################################################
###正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。先定义class：
class Student(object):
    pass


s = Student()
s.name = 'Michael'  # 动态给实例绑定一个属性
print s.name


###还可以尝试给实例绑定一个方法：
def set_age(self, age):  # 定义一个函数作为实例方法
    self.age = age


from types import MethodType

s.set_age = MethodType(set_age, s, Student)  # 给实例绑定一个方法
s.set_age(25)  # 调用实例方法
s.age  # 测试结果

###但是，给一个实例绑定的方法，对另一个实例是不起作用的：
s2 = Student()  # 创建新的实例
s2.set_age(25)  # 尝试调用方法
"""
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'set_age'
"""


###为了给所有实例都绑定方法，可以给class绑定方法：
def set_score(self, score):
    self.score = score


Student.set_score = MethodType(set_score, None, Student)

###给class绑定方法后，所有实例均可调用：
s.set_score(100)
s.score

s2.set_score(99)
s2.score


###使用__slots__但是，如果我们想要限制class的属性怎么办？比如，只允许对Student实例添加name和age属性。
###为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class能添加的属性：

class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


s = Student()  # 创建新的实例
s.name = 'Michael'  # 绑定属性'name'
s.age = 25  # 绑定属性'age'
s.score = 99  # 绑定属性'score'
"""
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'score'
"""


###由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。
###使用__slots__要注意，__slots__定义的属性仅对当前类起作用，对继承的子类是不起作用的：

class GraduateStudent(Student):
    pass


g = GraduateStudent()
g.score = 9999

###除非在子类中也定义__slots__，这样，子类允许定义的属性就是自身的__slots__加上父类的__slots__。
#############################################################################################
###定制类
__slot__  # 限制对象自定义属性的范围
__iter__  # 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法
__len__  # 能让class作用于len()函数
__str__  # 能使用"print obj"打印一个实例
__repr__  # 能使用"obj"打印一个实例
__name__  # 获取函数名
__author__  # 获取模块的作者
__doc__  # 获取包，模块，类，函数的文档
__getitem__
__setitem__
__delitem__
__getattr__
__setattr__
__delattr__

###Python的魔法函数之 - __len__,__getitem__,__setitem__,__delitem__

# 对象作为len()函数的参数是必须实现该方法
__len__
# 使用类似字典方式访问成员时必须实现 dic['pro_name']
__getitem__
# 使用类似字典方式设置成员时必须实现 dic['pro_name']='asdf'
__setitem__
# 使用类似字典方式删除成员时必须实现 delete dic['pro_name']
__delitem__


class DictDemo:
    def __init__(self, key, value):
        self.dict = {}
        self.dict[key] = value

    def __getitem__(self, key):
        return self.dict[key]

    def __setitem__(self, key, value):
        self.dict[key] = value

    def __len__(self):
        return len(self.dict)


dictDemo = DictDemo('key0', 'value0')
print(dictDemo['key0'])  # value0
dictDemo['key1'] = 'value1'
print(dictDemo['key1'])  # value1
print(len(dictDemo))  # 2


class storage(dict):
    # 通过使用__setattr__, __getattr__, __delattr__
    # 可以重写dict，使之通过“.”调用
    def __setattr__(self, key, value):
        self[key] = value

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError, k:
            return None

    def __delattr__(self, key):
        try:
            del self[key]
        except KeyError, k:
            return None

    # __call__方法用于实例自身的调用
    # 达到()调用的效果
    def __call__(self, key):
        try:
            return self[key]
        except KeyError, k:
            return None


s = storage()
s.name = "hello"  # 这是__setattr__起的作用
print s("name")  # 这是__call__起的作用
print s["name"]  # dict默认行为
print s.name  # 这是__getattr__起的作用
del s.name  # 这是__delattr__起的作用
print s("name")
print s["name"]
print s.name

#############################################################################################
"""
使用@property

在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改：

s = Student()
s.score = 9999

这显然不合逻辑。为了限制score的范围，可以通过一个set_score()方法来设置成绩，再通过一个get_score()来获取成绩，这样，在set_score()方法里，就可以检查参数：

class Student(object):

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

现在，对任意的Student实例进行操作，就不能随心所欲地设置score了：

>>> s = Student()
>>> s.set_score(60) # ok!
>>> s.get_score()
60
>>> s.set_score(9999)
Traceback (most recent call last):
  ...
ValueError: score must between 0 ~ 100!

但是，上面的调用方法又略显复杂，没有直接用属性这么直接简单。

有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢？对于追求完美的Python程序员来说，这是必须要做到的！

还记得装饰器（decorator）可以给函数动态加上功能吗？对于类的方法，装饰器一样起作用。Python内置的@property装饰器就是负责把一个方法变成属性调用的：

class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

@property的实现比较复杂，我们先考察如何使用。把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作：

>>> s = Student()
>>> s.score = 60 # OK，实际转化为s.set_score(60)
>>> s.score # OK，实际转化为s.get_score()
60
>>> s.score = 9999
Traceback (most recent call last):
  ...
ValueError: score must between 0 ~ 100!

注意到这个神奇的@property，我们在对实例属性操作的时候，就知道该属性很可能不是直接暴露的，而是通过getter和setter方法来实现的。

还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：

class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2014 - self._birth

上面的birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来。

"""

#############################################################################################


###判断是否为子类，是否为类的对象
issubclass(C, B)  # 是否是一个父类的子类
isinstance(object, class_or_type_or_tuple)  # 是否是一个类的对象
"""
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()
"""
hasattr(obj, 'x')  # 有属性'x'吗？
setattr(obj, 'y', 19)  # 设置一个属性'y'
getattr(obj, 'y')  # 获取属性'y'
hasattr(obj, 'power')  # 有属性'power'吗？
getattr(obj, 'power')  # 获取属性'power'
fn = getattr(obj, 'power')  # 获取属性'power'并赋值到变量fn
fn  # fn指向obj.power
#############################################################################################
###如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：
from collections import Iterable

isinstance('abc', Iterable)  # str是否可迭代
True
isinstance([1, 2, 3], Iterable)  # list是否可迭代
True
isinstance(123, Iterable)  # 整数是否可迭代
False
#############################################################################################
###正则表达式，子组，一组()代表一个分组
import re

m = re.match('(\w\w\w)-(\d\d\d)', 'xyz-123')
print m.group()
print m.group(1)
print m.group(2)
print m.groups()

m = re.match('((\w\w\w)-(\d\d\d))', 'xyz-123')
print m.group()
print m.group(1)
print m.group(2)
print m.group(3)
print m.groups()
#############################################################################################
###mysqldb只支持mysql数据库  
###sqlalchemy支持多种数据库模型
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import Column, Integer, String

##声明基类,创建engine
Base = declarative_base()
engine = create_engine('mysql://navi:123456@192.168.2.191/student')

##数据库连接session
Session = sessionmaker(bind=engine)
session = Session()


##不创建表，student数据库中已经有user表，user表必须包含id和name两个字段
class User(Base):
    ###连接数据库的user表
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    def __repr__(self):
        return "User(id={0},name={1})".format(self.id, self.name)


##查询
lstUser = session.query(User).all()
print lstUser
lstUser = session.query(User.name).all()
print lstUser

##分页查询
lstUser = session.query(User).limit(2).offset(0).all()
print lstUser
lstUser = session.query(User).all()[0:2]
print lstUser

##查询总数
print session.query(User.id).count()
from sqlalchemy import func

print session.query(func.count('*')).select_from(User).scalar()
print session.query(func.count(User.id)).scalar()

##查询
##equal，not equal
lstUser = session.query(User).filter(User.name == 'aaaa').all()
print lstUser
lstUser = session.query(User).filter(User.name != 'aaaa').all()
print lstUser

##like
lstUser = session.query(User).filter(User.name.like('%a%')).all()
print lstUser

##in 和 not in
lstUser = session.query(User).filter(User.name.in_(['aabb', 'abc'])).all()
print lstUser
lstUser = session.query(User).filter(~User.name.in_(['aabb', 'abc'])).all()
print lstUser

##and
from sqlalchemy import and_

lstUser = session.query(User).filter(User.name == 'aabb', User.name == 'abc').all()
print lstUser
lstUser = session.query(User).filter(and_(User.name == 'aabb', User.name == 'abc')).all()
print lstUser
lstUser = session.query(User).filter(User.name == 'aabb').filter(User.name == 'abc').all()
print lstUser

##or
from sqlalchemy import or_

lstUser = session.query(User).filter(or_(User.name == 'aabb', User.name == 'abc')).all()
print listUser

##null,not null
lstUser = session.query(User).filter(User.name == None).all()
print lstUser
lstUser = session.query(User).filter(User.name != None).all()
print lstUser

##数据集
lstUser = session.query(User).all()
print lstUser
lstUser = session.query(User).first()
print lstUser
lstUser = session.query(User).filter(User.id == 1).one()
print lstUser
lstUser = session.query(User.id).filter(User.id == 1).scalar()
print lstUser

##单表写入一行
user = User()
user.name = 'sqlalchemy'
session.add(user)
session.commit()

##单表写入多行
session.add_all([User(name='abc'), User(name='123')])
session.commit()


##创建表
class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True, autoincrement=True)
    userid = Column(Integer)
    email = Column(String(50))


Base.metadata.create_all(bind=engine)

##多表写入
user = User()
user.name = "addall"
address = Address()
address.userid = 1
address.email = "admin@tarean.com"
session.add_all([user, address])
session.commit()

##修改
user = session.query(User).get(1)
user.name = "abcabc"
session.add(user)
session.commit()

##删除
session.query(User).filter(User.name == 'aaaa').delete()
user = session.query(User).get(5)
session.delete(user)
session.commit()

##外键,必须先删除上面的Address表
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Address(Base):
    __tablename__ = "addresses"
    id = Column(Integer, primary_key=True)
    email_address = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="address")


User.address = relationship("Adderss", order_by=Address.id, back_populates="user")
Base.metadata.create_all(bind=engine)
##外键查询
user = session.query(User).get(1)
print user.address

##扩展
from datetime import datetime
from sqlalchemy.orm.interfaces import MapperExtension


class DataUpdateExtension(MapperExtension):
    def before_update(self, mapper, connection, instance):
        if hasattr(instance, "UpdateTime"):
            instance.UpdateTime = datetime.now()

    def before_insert(self, mapper, connection, instance):
        if hasattr(instance, "CreateTime"):
            instance.CreateTime = datetime.now()
        if hasattr(instance, "UpdateTime"):
            instance.UpdateTime = instance.CreateTime


class Address(Base):
    __tablename__ = "address_1"
    __mapper_args__ = {"extension": DataUpdateExtension()}
    id = Column(Integer, primary_key=True)
    email_address = Column('email', String(50), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"))
    UpdateTime = Column(DateTime)
    CreateTime = Column(DateTime)


Base.metadata.create_all(bind=engine)

address = session.query(Address).filter(Address.id == 1).first()
address.email_address = 'c@a.com'
session.add(address)
session.commit()

##中间件
cobar, atlas, tddl
#############################################################################################
###多进程
# fork创建一个子进程
import os

print 'Process (%s) start...' % os.getpid()
pid = os.fork()
if pid == 0:
    print 'I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid())
else:
    print 'I (%s) just created a child process (%s).' % (os.getpid(), pid)

"""
运行结果如下：

Process (876) start...
I (876) just created a child process (877).
I am child process (877) and my parent is 876.

"""
# ----------------------------------------------------------------------------------------------
# multiprocessing中的process创建一个子进程
from multiprocessing import Process
import os


# 子进程要执行的代码
def run_proc(name):
    print 'Run child process %s (%s)...' % (name, os.getpid())


if __name__ == '__main__':
    print 'Parent process %s.' % os.getpid()
    p = Process(target=run_proc, args=('test',))
    print 'Process will start.'
    p.start()
    p.join()
    print 'Process end.'

"""
执行结果如下：

Parent process 928.
Process will start.
Run child process test (929)...
Process end.

"""
# ----------------------------------------------------------------------------------------------
# multiprocessing中pool创建多个子进程
from multiprocessing import Pool
import os, time, random


def long_time_task(name):
    print 'Run task %s (%s)...' % (name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))


if __name__ == '__main__':
    print 'Parent process %s.' % os.getpid()
    p = Pool()
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print 'Waiting for all subprocesses done...'
    p.close()
    p.join()
    print 'All subprocesses done.'

"""
执行结果如下：

Parent process 669.
Waiting for all subprocesses done...
Run task 0 (671)...
Run task 1 (672)...
Run task 2 (673)...
Run task 3 (674)...
Task 2 runs 0.14 seconds.
Run task 4 (673)...
Task 1 runs 0.27 seconds.
Task 3 runs 0.86 seconds.
Task 0 runs 1.41 seconds.
Task 4 runs 1.91 seconds.
All subprocesses done.

"""
# ----------------------------------------------------------------------------------------------
# multiprocessing的queue实现进程之间相互通信
from multiprocessing import Process, Queue
import os, time, random


# 写数据进程执行的代码:
def write(q):
    for value in ['A', 'B', 'C']:
        print 'Put %s to queue...' % value
        q.put(value)
        time.sleep(random.random())


# 读数据进程执行的代码:
def read(q):
    while True:
        value = q.get(True)
        print 'Get %s from queue.' % value


if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()

##########################################################################################
###多线程
import time, threading


# 新线程执行的代码:
def loop():
    print 'thread %s is running...' % threading.current_thread().name
    n = 0
    while n < 5:
        n = n + 1
        print 'thread %s >>> %s' % (threading.current_thread().name, n)
        time.sleep(1)
    print 'thread %s ended.' % threading.current_thread().name


print 'thread %s is running...' % threading.current_thread().name
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print 'thread %s ended.' % threading.current_thread().name

"""
执行结果如下：

thread MainThread is running...
thread LoopThread is running...
thread LoopThread >>> 1
thread LoopThread >>> 2
thread LoopThread >>> 3
thread LoopThread >>> 4
thread LoopThread >>> 5
thread LoopThread ended.
thread MainThread ended.

"""

# ----------------------------------------------------------------------------------------------
###lock
"""
Lock

多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。

来看看多个线程同时操作一个变量怎么把内容给改乱了：
"""
import time, threading

# 假定这是你的银行存款:
balance = 0


def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(100000):
        change_it(n)


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print balance

"""
我们定义了一个共享变量balance，初始值为0，并且启动两个线程，先存后取，理论上结果应该为0，但是，由于线程的调度是由操作系统决定的，当t1、t2交替执行时，只要循环次数足够多，balance的结果就不一定是0了。

原因是因为高级语言的一条语句在CPU执行时是若干条语句，即使一个简单的计算：

balance = balance + n

也分两步：

    计算balance + n，存入临时变量中；
    将临时变量的值赋给balance。

"""
# ----------------------------------------------------------------------------------------------
import time, threading

# 假定这是你的银行存款:
balance = 0
lock = threading.Lock()


def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print balance

# ----------------------------------------------------------------------------------------------
# ThreadLocal

import threading

# 创建全局ThreadLocal对象:
local_school = threading.local()


def process_student():
    print 'Hello, %s (in %s)' % (local_school.student, threading.current_thread().name)


def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()


t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()

"""
执行结果：

Hello, Alice (in Thread-A)
Hello, Bob (in Thread-B)
"""
# ----------------------------------------------------------------------------------------------
###分布式进程
# taskmanager.py

import random, time, Queue
from multiprocessing.managers import BaseManager

# 发送任务的队列:
task_queue = Queue.Queue()
# 接收结果的队列:
result_queue = Queue.Queue()


# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass


# 把两个Queue都注册到网络上, callable参数关联了Queue对象:
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)
# 绑定端口5000, 设置验证码'abc':
manager = QueueManager(address=('', 5000), authkey='abc')
# 启动Queue:
manager.start()
# 获得通过网络访问的Queue对象:
task = manager.get_task_queue()
result = manager.get_result_queue()
# 放几个任务进去:
for i in range(10):
    n = random.randint(0, 10000)
    print('Put task %d...' % n)
    task.put(n)
# 从result队列读取结果:
print('Try get results...')
for i in range(10):
    r = result.get(timeout=10)
    print('Result: %s' % r)
# 关闭:
manager.shutdown()

# taskworker.py

import time, sys, Queue
from multiprocessing.managers import BaseManager


# 创建类似的QueueManager:
class QueueManager(BaseManager):
    pass


# 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 连接到服务器，也就是运行taskmanager.py的机器:
server_addr = '127.0.0.1'
print('Connect to server %s...' % server_addr)
# 端口和验证码注意保持与taskmanager.py设置的完全一致:
m = QueueManager(address=(server_addr, 5000), authkey='abc')
# 从网络连接:
m.connect()
# 获取Queue的对象:
task = m.get_task_queue()
result = m.get_result_queue()
# 从task队列取任务,并把结果写入result队列:
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d...' % (n, n))
        r = '%d * %d = %d' % (n, n, n * n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('task queue is empty.')
# 处理结束:
print('worker exit.')
##########################################################################################
import importlib

##导入"test.py"变成module1模块
module1 = importlib.import_module("demo.py")
##等同于
import demo as module1
