#!/usr/bin/env python
# coding:utf-8

import codecs

"""
u = u'中文'                  #显示指定unicode类型对象u
str = u.encode('gb2312')    #以gb2312编码对unicode对像进行编码
str1 = u.encode('gbk')       #以gbk编码对unicode对像进行编码
str2 = u.encode('utf-8')     #以utf-8编码对unicode对像进行编码
u1 = str.decode('gb2312')    #以gb2312编码对字符串str进行解码，以获取unicode
u2 = str.decode('utf-8')     #如果以utf-8的编码对str进行解码得到的结果，将无法还原原来的unicode类型
"""

content = u"中文"
assert isinstance(content,unicode)
f = codecs.open("./files/tmp.txt","w","utf-8")
f.write(content)