#coding:utf-8

"""
file,open,with open as...
"""

#1)file和open (filename,mode) mode可以是r,w,a,read和readlines区别是，read返回字符串，readlines返回列表
f = file("file.txt","r")
ret01 = f.read()
f.close()

f = file("file.txt","r")
ret02 = f.readlines()
f.close()

print ret01
print
print ret02

f = file("file.txt","a")
f.write("append a line\n")
f.close()

f = file("file.txt","w")
f.write("everything is covered\n")
f.close()

f = open("file.txt","r")
ret03 = f.read()
f.close()

f = open("file.txt","r")
ret04 = f.readlines()
f.close()

print ret03
print
print ret04

f = open("file.txt","a")
f.write("append a line\n")
f.close()

f = open("file.txt","w")
f.write("everything is converd\n")
f.close()

#2) with open() as ...
with open("file.txt","r") as fd:
    for line in fd:
        print line

with open('data') as fin,open('res','w') as fout:
    for line in fin:
        if 'some key' in line:
            fout.write(line)