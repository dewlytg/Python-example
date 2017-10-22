#coding:utf-8

"""
python3中
try:
    module = raw_input("请输入你想导入的模块？")
    __import__(module)
except IndentationError as e:
    print e
except IOError as e:
    print e
except TypeError as e:
    print e
except Exception as e:
    print e
else:
    print "导入成功！"
finally:
    print "结束！"
"""

###try 异常处理
try:
    module = raw_input("请输入你想导入的模块？")
    __import__(module)
except IndentationError,e:
    print e
except IOError,e:
    print e
except TypeError,e:
    print e
except Exception,e:
    print e
else:
    print "导入成功！"
finally:
    print "结束！"

###自定义异常
class MyError(Exception):
    def __init__(self,msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    raise MyError("自定义异常只能手动出发，而系统异常可以在代码执行的过程中自动出发")
except MyError,e:
    print e
