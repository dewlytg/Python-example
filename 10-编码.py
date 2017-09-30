#coding:utf-8

"""
——————————————————————————————————————————————————
acsii       单字节编码，只能存英文字母
unicode     双字节编码，可以存任意字符
utf8        可变字节编码，unicode的扩展，也可以存任意字符，如果是英文字符就只占一个字符，中文三个字符
----------------------------------------------------------------------------------------------------
gbk,euc,koi8        各国语言的不同编码

str1 = "中国"         这样定义的字符串是UTF-8，因为第一行coding指定了
str_to_unicode = str1.decode("utf-8")       字符串只能解码变成unicode编码，小括号内要指定字符串现在的编码
unicode_to_gbk = str_to_unicode.encode("gbk")       unicode又变成括号内指定的编码

上述例子可以看出unicode的重要性，它是字符集转换的中间集，也是支持全世界所有字符集的根本

u1 = u"中国"      这样定义的字符串是unicode，因为前面加了u，即使我们赋的值是中文

"""

import codecs

u = u'中文'                  #显示指定unicode类型对象u
str1 = u.encode('gb2312')    #以gb2312编码对unicode对像进行编码
str2 = u.encode('gbk')       #以gbk编码对unicode对像进行编码
str3 = u.encode('utf-8')     #以utf-8编码对unicode对像进行编码
u1 = str1.decode('gb2312')    #以gb2312编码对字符串str进行解码，以获取unicode
u2 = str2.decode('utf-8')     #如果以utf-8的编码对str进行解码得到的结果，将无法还原原来的unicode类型

###写入中文到文件
content = u"中文"
assert isinstance(content,unicode)
f = codecs.open("./files/tmp.txt","w","utf-8")
f.write(content)
f.close()
