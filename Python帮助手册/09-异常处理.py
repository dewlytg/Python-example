#coding:utf-8

###try 异常处理
try:
    module = raw_input("请输入你想导入的模块？")
    __import__(module)
except Exception,e:
    print e
else:
    print "导入成功！"
finally:
    print "结束！"