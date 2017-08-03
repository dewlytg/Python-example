#coding:utf-8

###ConfigParser模块
import ConfigParser

###生成config对象
conf = ConfigParser.ConfigParser()

###用config对象读取配置文件
conf.read("config.ini")

###以列表形式返回所有的section
sections = conf.sections()
print 'sections:', sections

###得到指定section的所有option
options = conf.options("user")
print 'options:', options

###得到指定section的所有键值对
useritem = conf.items("user")
print 'user:', useritem

###指定section，option读取值
str_val = conf.get("book", "bookname")
int_val = conf.getint("book", "bookprice")

print "value for book's bookname:", str_val
print "value for book's bookprice:", int_val

###更新和写入指定section，option的值
conf.set("book", "bookname", "python learning")
conf.set("book", "bookpress", "人民邮电出版社")

###增加新的section
conf.add_section('purchaser')
conf.set('purchaser', 'count', '1')

###写回配置文件
conf.write(open("config.ini", "w"))
