#coding:utf-8

"""
Python 日期和时间
Python 程序能用很多方式处理日期和时间，转换日期格式是一个常见的功能。
Python 提供了一个 time 和 calendar 模块可以用于格式化日期和时间。
时间间隔是以秒为单位的浮点小数。
每个时间戳都以自从1970年1月1日午夜（历元）经过了多长时间来表示。
Python 的 time 模块下有很多函数可以转换常见日期格式。如函数time.time()用于获取当前时间戳, 如下实例:
"""
import time
ticks = time.time()
print "当前时间戳：",ticks

"""
获取当前时间
从返回浮点数的时间辍方式向时间元组转换，只要将浮点数传递给如localtime之类的函数。

tm_year                 年
tm_mon                  月
tm_mday                 日
tm_hour                 时
tm_min                  分
tm_sec                  秒
tm_wday                 周，从0开始
tm_yday                 一年的第多少天
tm_isdst                -1, 0, 1, -1是决定是否为夏令时的旗帜
"""
##从返回浮点数的时间辍方式向时间元组转换，只要将浮点数传递给如localtime之类的函数
localtime = time.localtime()
print "本地时间为：",localtime

##你可以根据需求选取各种格式，但是最简单的获取可读的时间模式的函数是asctime()
flocaltime = time.asctime(time.localtime())
print "本地时间为：",flocaltime

##我们可以使用 time 模块的 strftime 方法来格式化日期
print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
print time.strftime("%a %b %d %H:%M:%S %Y",time.localtime())
a = "Sat Mar 28 22:24:24 2016"
print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))


"""
获取某月日历
Calendar模块有很广泛的方法用来处理年历和月历，例如打印某月的月历：
"""
import calendar

cal = calendar.month(2016,1)
print "以下输出2016年1月份的日志："
print cal


###使用datetime模块来获取当前的日期和时间
import datetime
i = datetime.datetime.now()
print ("当前的日期和时间是 %s" % i)
print ("ISO格式的日期和时间是 %s" % i.isoformat())
print ("当前的年份是 %s" %i.year)
print ("当前的月份是 %s" %i.month)
print ("当前的日期是  %s" %i.day)
print ("dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year))
print ("当前小时是 %s" %i.hour)
print ("当前分钟是 %s" %i.minute)
print ("当前秒是  %s" %i.second)

##获取昨天，今天和明天的日期
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)
print "昨天：",yesterday
print "今天：",today
print "明天：",tomorrow