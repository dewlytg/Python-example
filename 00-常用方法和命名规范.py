#coding:utf-8

type()          # 查询对象类型
id()            # 查询对象在内存中的位置
help()          # 获取帮助
raw_input()     # 输入
chr()           # 将整数转为字符
ord()           # 将字符转换为整数值
hex()           # 将整数转换为16进制字符
bin()           # 将整数转换为2进制字符
oct()           # 将整数转换为8进制字符
range(10)       # 获取列表
xrange()        # xrange() 类似 range() , 不过当你有一个很大的范围列表时, xrange() 可能更为适合, 因为它不会在内存里创建列表的完整拷贝. 它只被用在 for 循环中, 在 for 循环外使用它没有意义
max()           # 获取对象最大值
min()           # 获取对象最小值
len()           # 获取对象长度
sum()           # 获取对象的和值
any()           # 一个为真即为真
all()           # 所有为真才为真
abs()           # 绝对值
pow()           # 平方值
round()         # 四舍五入
coerce()        #  将 num1 和 num2 转换为同一类型，然后以一个元组的形式返回
divmod()        # 除法求余
dir()           # 列出对象所有属性和方法
enumerate()     # 枚举对象
cmp()           # 比较两个对象大小
exec("import os")  # 可执行语句组[和 exec 一起使用]
eval("[1,2,3]") # 可求值的表达式[和 eval()一起使用]
issubclass()    # 判断是否为子类
isinstance()    # 判断是否为制定类的实例
hasattr()       # 判断是否对象有制定属性
hash()          # 所有不可变的类型都是可哈希的，因此它们都可以做为字典的键
apply()         # apply(func,*args,**kwargs)

"""
Python之父Guido推荐的规范
Type                        Public	                                  Internal
Modules                     lower_with_under                        _lower_with_under
Packages                    lower_with_under
Classes                     CapWords 	                            _CapWords
Exceptions                  CapWords
Functions                   lower_with_under()                      _lower_with_under()
Global/Class Constants 	    CAPS_WITH_UNDER 	                    _CAPS_WITH_UNDER
Global/Class Variables 	    lower_with_under 	                    _lower_with_under
Instance Variables          lower_with_under 	                    _lower_with_under (protected) or __lower_with_under (private)
Method Names                lower_with_under() 	                    _lower_with_under() (protected) or __lower_with_under() (private)
Function/Method Parameters  lower_with_under
Local Variables             lower_with_under
"""
