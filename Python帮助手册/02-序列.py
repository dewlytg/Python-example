#coding:utf-8

"""
序列：字符,元组,列表
所有序列都支持迭代
序列表示索引为非负整数的有序对象集合
字符和元组属于不可变序列,列表可变
"""

#1)字符
str1 = "hello,world!"
str2 = "HELLO,WORLD!"
str3 = "a b c d e f g"

##运算符：
"""
    索引运算：       s[i]          返回序列的第i个元素
    切片运算：       s[i:j]        返回序列的从i开始到j结束的元素
    步进切片运算：    s[i:j:stride] 
"""

print str1[0]
print str1[0:5]
print str1[0:5:2]

##运算:索引,切片,min(),max(),len()等,最大值最小值是通过ord()函数获取的
"""
    len(s)      s中的元素个数
    min(s)      s中的最小值
    max(s)      s中的最大值
    s.upper()   将字符串转换为大写
    s.lower()   将字符串转换为小写
    "\t".join(s)   用"\t"把字符串s连接
    s.split()   以空格分割字符串,变成列表
    s.replace(old,new) 将字符串s中的值替换
"""

print len(str1)
print min(str1)
print max(str1)
print str1.upper()
print str2.lower()
print "\t".join(str1)
print str3.split()
print str1.replace("hello","Hello")


#2)列表
l1 = [1,2,3,4,5,1,2,3,4,1,2,3,1,2,1]
l2 = ["a","b","c","d","e"]
"""
    list.count(value)    统计元素在列表出现的次数
    list.append(value)   向列表末尾追加元素
    list.extend(otherlist)   合表另外一个列表到现在的列表
    list.insert(index,value) 在指定index处插入元素
    list.sort()              列表排序
    list.reverse()           列表排倒序
    list.pop(index)          删除列表中指定索引的元素
    list.remove(value)       只删除列表中从左开始算第一个元素
"""
print l1[1]
print len(l1)
print min(l1)
print max(l1)
print l1.count(1)
l1.append("abc")
print l1
l1.extend(l2)
print l1
l1.insert(1,"xyz")
print l1
l1.sort()
print l1
l1.reverse()
print l1
l1.pop(0)
print l1
l1.remove(4)
print l1
l1.remove(1)
print l1

#3)元组：
t1 = (1,2,3,"abc","xyz")
print 1 in t1
print 5 not in t1

##虽然元组本身不可变，但如果元组内嵌套了可变类型的元素，那么此类元素的修改不会返回新元组
t2 = (1,2,3,[2,4,6])
print t2
print id(t2)
print t2[3]
t2[3].pop()
print t2
print id(t2)

