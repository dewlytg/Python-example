#coding:utf-8

#1）标准算术运算符
"""
+   -   *   /   //  %   **
"""
print 5 + 2
print 5 - 2
print 5 * 2
print 5.0 / 2
print 5.0 // 2
print 5 ** 2

#2）标准比较运算符
"""
<   <=  >   >=  ==  !=  <>
"""
print 2 < 5
print 2 <= 5
print 2 > 5
print 2 >= 5
print 2 == 5
print 2 != 5
print 2 <> 5

#3）逻辑运算符
"""
and or  not
"""
print 2 < 5 and 2 == 5
print 2 < 5 or 2 > 5
print not 2 < 5
print 2 < 5 < 8


#4）位运算符
"""
<<  >>  &   ^   |
"""
num1 = 10
num2 = 2
~ num1          # 单目运算，对数的每一位取反
num1 << num2    # num1 左移 num2 位
num1 >> num2    # num1 右移 num2 位
num1 & num2     # num1 与 num2
num1 | num2     # num1 与 num2 或
num1 ^ num2     # num1 异或 num2
#下面是几个使用整数 30(011110)，45(101101)，60(111100)进行位运算的例子:
print 30 & 45
print 45 & 60
print 30 | 45
print ~30
print 45 << 1
print 60 >> 2
print 30 ^ 45
