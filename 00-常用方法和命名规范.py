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
max()           # 获取对象最大值
min()           # 获取对象最小值
len()           # 获取对象长度
sum()           # 获取对象的和值
any()           # 一个为真即为真
all()           # 所有为真才为真
divmod()        # 除法求余
dir()           # 列出对象所有属性和方法
enumerate()     # 枚举对象
cmp()           # 比较两个对象大小
eval("[1,2,3]") # 将字符串str当成有效的表达式来求值并返回计算结果
issubclass()    # 判断是否为子类
isinstance()    # 判断是否为制定类的实例
hasattr()       # 判断是否对象有制定属性


"""
Python之父Guido推荐的规范
Type                        Public	                                  Internal
Modules                     lower_with_under                        _lower_with_under
Packages                    lower_with_under
Classes                     CapWords 	                              _CapWords
Exceptions                  CapWords
Functions                   lower_with_under()                      _lower_with_under()
Global/Class Constants 	    CAPS_WITH_UNDER 	                       _CAPS_WITH_UNDER
Global/Class Variables 	    lower_with_under 	                    _lower_with_under
Instance Variables          lower_with_under 	                    _lower_with_under (protected) or __lower_with_under (private)
Method Names                lower_with_under() 	                    _lower_with_under() (protected) or __lower_with_under() (private)
Function/Method Parameters  lower_with_under
Local Variables             lower_with_under
"""
