#coding:utf-8
"""
字符
.    匹配除换行符以外的任意字符                  a.c        abc
\    转义符                                      a\.c       a.c
[]   用来匹配一个指定的字符类别                  a[bcd]e    abe 或 ace 或 ade

数量词
+    匹配一次或者无限次                          abc+        abc 或 abccc
？   对于前一个字符字符重复0次到1次              abc?        ab 或 abc
*    对于前一个字符重复0次到无穷次               abc*        ab 或 abccc
{}   对于前一个字符重复m次                       ab{2}c      abbc
{m，n} 对前一个字符重复为m到n次                  ab{1,2}c    abc

预定义字符集
\d   匹配数字，相当于[0-9]                       a\dc         a1c
\D   匹配任何非数字字符，相当于[^0-9]            a\Dc         abc
\s   匹配任意的空白符，相当于[ fv]               a\sc         a c
\S   匹配任何非空白字符，相当于[^ fv]            a\Sc         abc
\w   匹配任何字母数字字符，相当于[a-zA-Z0-9_]    a\wc         abc
\W   匹配任何非字母数字字符，相当于[^a-zA-Z0-9_] a\Wc         a c

边界匹配
^    匹配字符串的开始                            ^abc         abc
$    匹配字符串的结束                            abc$         abc
\A   仅匹配字符串开头                            \Aabc        abc
\Z   仅匹配字符串结尾                            abc\Z        abc
\b   匹配单词的开始或结束
     左边界匹配              "\bthe"      "bit thedog"
     右边界匹配              "the\b"      "bitthe dog"
     左右边界匹配            "\bthe\b"    "bit the dog"
\B   [^\b]                   "\Bthe"       "bitthe dog"

逻辑和分组
|     匹配左右任意一个                                 abc|def       abc 或 def
()    分组                                             (abc){2}      abcabc
(?P<name>....) 分组,并且给一个额外的别名               (?P<id>abc){2}  abcabc
(?P=name) 引用别名为<name>的分组批准的字符串           (?P<id>\d)abc(?P=id)  1abc1 或 5abc5
\<number> 引用编号为<number>的分组匹配到的字符串       (\d)abc\1       1abc1 或 5abc5



re.I(re.IGNORECASE): 忽略大小写（括号内是完整写法，下同）
   M(MULTILINE): 多行模式，改变'^'和'$'的行为（参见上图）
   S(DOTALL): 点任意匹配模式，改变'.'的行为
   L(LOCALE): 使预定字符类 \w \W \b \B \s \S 取决于当前区域设定
   U(UNICODE): 使预定字符类 \w \W \b \B \s \S \d \D 取决于unicode定义的字符属性
   X(VERBOSE): 详细模式。这个模式下正则表达式可以是多行，忽略空白字符，并可以加入注释。以下两个正则表达式是等价的：

"""
import  re
a = re.compile (r"""\d +  # the integral part
                \.    # the decimal point
                \d *  # some fractional digits""", re.X)
b = re.compile (r"\d+\.\d*")

#1)
"""
    math 只能从开头匹配，且只匹配一个
    search 从头到尾匹配，也只匹配一个
    findall 从头到尾匹配多个，返回列表
"""
pattern = re.compile(r"hello")
match = pattern.match("hello,world!")
if match:
    print match.group()

search = pattern.search("abc hello,world! hello")
if search:
    print search.group()

findall = pattern.findall("abc hello,world! hello")
print findall

#2)
m = re.match(r"(\w+) (\w+)(?P<sign>.*)","hello world!")
print "m.string:",m.string
print "m.re:",m.re
print "m.pos:",m.pos
print "m.endpos:",m.endpos
print "m.lastindex:",m.lastindex
print "m.lastgroup:",m.lastgroup

print "m.group(1,2):",m.group(1,2)
print "m.groups():",m.groups()
print "m.groupdict():",m.groupdict()
print "m.start(2):",m.start(2)
print "m.end(2):",m.end(2)
print "m.span(2):",m.span(2)
print r"me.expand(r'\2 \1\3'):",m.expand(r'\2 \1\3')


#3) split
p = re.compile(r"\d+")
print p.split("one1two2three3four4")

#4) sub
print re.sub("[0-9]+","|","ab12cd3ef55g")