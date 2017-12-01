#!/usr/bin/env python

"""
pymysql 和 mysqldb 模块语法很像
"""

import pymysql

#创建连接
conn = pymysql.connect(host="192.168.2.210",port=3306,user="root",password="123456",db="oldboydb")

#创建游标
cursor = conn.cursor()

#执行SQL,并返回受影响行
# cursor.execute("select * from student")
# data = cursor.fetchall()
# print(data)

data = [
    ("N1","2017-01-01","X"),
    ("N2","2017-01-10","Y"),
    ("N3","2017-11-11","X"),
]

cursor.executemany("insert into student(name,register_date,gender) values(%s,%s,%s)" , data)

conn.commit()
