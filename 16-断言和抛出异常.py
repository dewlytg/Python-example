#coding:utf-8

##raise 抛出异常
"""
使用raise抛出异常当程序出现错误，python会自动引发异常，也可以通过raise显示地引发异常。一旦执行了raise语句，raise后面的语句将不能执行
"""

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
"""
mylist = ["item"]
assert len(mylist) >= 1
mylist.pop()
assert len(mylist) >= 1