#!/usr/bin/env python

"""
FTP 对象的方法
方法                                             描述
login(user='anonymous',passwd='', acct='')       登录到 FTP 服务器，所有的参数都是可选的
pwd()                                            得到当前工作目录
cwd(path)                                        把当前工作目录设置为 path
dir([path[,...[,cb]])                            显示 path 目录里的内容，可选的参数 cb 是一个回调函数，它会被传给 retrlines()方法
nlst([path[,...])                                与 dir()类似，但返回一个文件名的列表，而不是显示这些文件名
retrlines(cmd [, cb])  							 给定 FTP 命令（如“RETR filename”），用于下载文本文件。可选的回调函数 cb 用于处理文件的每一行
retrbinary(cmd, cb[,bs=8192[, ra]]) 			 与 retrlines()类似，只是这个指令处理二进制文件。回调函数cb用于处理每一块（块大小默认为 8K）下载的数据。
storlines(cmd, f)  								 给定 FTP 命令（如“STOR filename”），以上传文本文件。要给定一个文件对象 f
storbinary(cmd, f[,bs=8192]) 					 与 storlines()类似，只是这个指令处理二进制文件。要给定一个文件对象 f，上传块大小 bs 默认为 8Kbs=8192])
rename(old, new)                                 把远程文件 old 改名为 new
delete(path)                                     删除位于 path 的远程文件
mkd(directory)                                   创建远程目录
rmd(directory)                                   删除远程目录
quit()                                           关闭连接并退出
在一般的 FTP 通讯中，要使用到的指令有 login(), cwd(), dir(), pwd(), stor*(), retr*()
和 quit()。有一些没有列出的 FTP 对象方法也是很有用的。请参阅 Python 的文档以得到更多关于
FTP 对象的信息：
http://python.org/docs/current/lib/ftp-objects.html

"""


import ftplib
import os
import socket

HOST = "ftp.mozilla.org"
DIRN = "pub/mozilla.org/webtools"
FILE = "bugzilla-LATEST.tar.gz"

def main():
    try:
        f = ftplib.FTP(HOST)
    except (socket.error,socket.gaierror),e:
        print "ERROR: cannot reach %s " % HOST
        return
    print "*** Connected to host %s" % HOST

    try:
        f.login()
    except ftplib.error_perm:
        print "ERROR: cannot login anonymously"
        f.quit()
        return
    print "*** Logged in as anonymous"

    try:
        f.cwd(DIRN)
    except ftplib.error_perm:
        print "ERROR: cannot CD to %s" % DIRN
        f.quit()
        return
    print "*** Changed to %s folder" % DIRN

    try:
        f.retrbinary("RETR %s" % FILE,open(FILE,"wb").write)
    except ftplib.error_perm:
        print "ERROR: cannot read file %s" % FILE
        os.unlink(FILE)
    else:
        print "*** Downloaded %s to CWD" % FILE
        f.quit()
        return

if __name__ == "__main__":
    main()