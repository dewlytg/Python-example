#!/usr/bin/env python
#coding:utf-8

import datetime
"""
If you want to convert string for unicode,please use str.decode,other you want to convert
unicode to string , please use encode.
"""

__author__ = "dewly_tg"

def tuple2str(tup):
    result = ""
    length = len(tup)
    for i in range(length):
        if type(tup[i]) == long:
            col_long =  bytes(tup[i])
            result = result + col_long + "\t"
        elif type(tup[i]) == datetime.datetime:
            col_date = str(tup[i])
            result = result + col_date + "\t"
        else:
            result = result + tup[i] + "\t"
    ret = result.rstrip("\t").encode ("utf-8")
    return ret

