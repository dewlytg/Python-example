#coding:utf-8

##tip:变量名必须是大小写英文、数字和_的组合，且不能用数字开头

##字符串声明方式,None代表空值,一个特殊的字符
str1 = "abc"
str2 = str("abc")
str3 = None
print str1,str2,str3

##整数声明方式,长整型数字声明数字后面加L即可,整数转换为字符串类型str(),长整类型转换为字符串类型使用bytes()
int1 = 123
int2 = int(123)
longint3 = 123L
print int1,int2,longint3
print type(int1),type(int2),type(longint3)
print str(int1),str(int2),bytes(longint3)
print type(str(int1)),type(str(int2)),type(bytes(longint3))

##浮点型声明方式,浮点型转换为字符串str(),科学计数法声明，把10用e替代，1.23x109就是1.23e9
float1 = 123.01
float2 = float(123.01)
float3 = 1.23e9
print float1,float2,float3
print type(float1),type(float2),type(float3)
print str(float1),str(float2),str(float3)
print type(str(float1)),type(str(float2)),type(str(float3))

##布尔值True和Flase,布尔值可以用and、or和not运算,None代表空值，返回Flase，非空则返回True,非0整数返回True,0返回Flase
True and True
True and False
False and False

True or True
True or False
False or False

not True
not False

##常用运算,注意："="代表赋值,"=="代表判断左右两个值是否相等,"is"也可以判断左右两个值是否相等
print int1 + int2
print int1 - int2
print int1 * 10
print int2 % 2
int1 is int2
int1 == int2
str1 is str1
int1 == int2

##格式化字符串,%s代表字符串,%d代表整数类型,%f代表浮点型数,%后可以使用%+数字,+号可以省略,或者%-数字,表示左右空格多少个整数的位置
print "你的名字是：%s" % "Tom"
print "你的年龄是：%d" % 32
print "你的收入是：%f" % 10000.123
print "你的名字是：{0},你的年龄是：{1},你的收入是：{2}".format("tom",32,10000.123)


##字符串对齐
str1 = "中国人"
print str1.center(100)
print str1.ljust(100)
print str1.rjust(100)

