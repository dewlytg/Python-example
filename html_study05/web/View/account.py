#!/usr/bin/env python

def handler_index():
    fd = open("Template/index.html","rb")
    data = fd.read()
    fd.close()
    return [data,]

def handler_date():
    return [b"<h1>hello,date!</h1>",]
