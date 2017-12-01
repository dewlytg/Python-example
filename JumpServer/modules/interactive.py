# Copyright (C) 2003-2007  Robey Pointer <robeypointer@gmail.com>
#
# This file is part of paramiko.
#
# Paramiko is free software; you can redistribute it and/or modify it under the
# terms of the GNU Lesser General Public License as published by the Free
# Software Foundation; either version 2.1 of the License, or (at your option)
# any later version.
#
# Paramiko is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Paramiko; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA.


import socket
import sys
import select
from paramiko.py3compat import u
from  modules import models
import datetime

# windows does not have termios...
try:
    import termios
    import tty
    has_termios = True
except ImportError:
    has_termios = False


def interactive_shell(chan,user_obj,bind_host_obj,cmd_logs,log_recording):
    if has_termios:
        posix_shell(chan,user_obj,bind_host_obj,cmd_logs,log_recording)
    else:
        windows_shell(chan)


def posix_shell(chan,user_obj,bind_host_obj,cmd_logs,log_recording):
    # 获取原tty属性
    oldtty = termios.tcgetattr(sys.stdin)
    try:
        # 为tty设置新属性
        # 默认当前tty设备属性：
        # 输入一行回车，执行
        # CTRL+C 进程退出，遇到特殊字符，特殊处理。

        # 这是为原始模式，不认识所有特殊符号
        # 放置特殊字符应用在当前终端，如此设置，将所有的用户输入均发送到远程服务器
        tty.setraw(sys.stdin.fileno())
        tty.setcbreak(sys.stdin.fileno())
        chan.settimeout(0.0)
        cmd = ''

        tab_key = False
        # 注意，下面循环其实是先循环 if sys.stdin in r:(用户先有输入)，后面循环if chan in r:(放回结果，tab键补全的内容也是返回结果)
        while True:
            r, w, e = select.select([chan, sys.stdin], [], [])
            if chan in r:
                try:
                    x = u(chan.recv(1024))
                    # 如果用户上一次点击的是tab键，则获取返回的内容写入在记录中
                    if tab_key:
                        #if x not in ('\x07' , '\r\n'):
                        cmd += x # 这里会记录一个tab键加上tab后面的stdout
                        tab_key = False
                    if len(x) == 0:
                        sys.stdout.write('\r\n*** EOF\r\n')
                        break
                    sys.stdout.write(x)
                    sys.stdout.flush()
                except socket.timeout:
                    pass
            if sys.stdin in r:
                # 因为要使用tab键，所以一个字节一个字节的去读取数据
                x = sys.stdin.read(1)
                # 用户输入命令的时候没有输入回车，比如ifconfig，会依次循环收取i,f,c,o,n，此时再输入tab键，会循环到下面的if x == "\t":判断，tab键补全的内容就是标准输出了，stdout会走到上面的循环中去，if tab_key
                if x != "\r":
                    cmd += x
                else: # 这里用户输入了回车，一条命令执行完毕
                    log_item = models.AuditLog(user_id=user_obj.id,
                                          bind_host_id=bind_host_obj.id,
                                          action_type='cmd',
                                          cmd=cmd.replace("\t",""), #替换掉命令中的tab空格
                                          date=datetime.datetime.now()
                                          )
                    cmd_logs.append(log_item)
                    cmd = ""
                    if len(cmd_logs)>= 10:
                        #log_recording(user_obj,bind_host_obj,cmd_caches) #貌似user_obj，bind_host_obj和cmd_caches中的有些字段重复了
                        log_recording(cmd_logs) # 记录用户日志，每十条写一次数据库
                        cmd_logs = []
                if x == "\t": # 用户输入tab
                    tab_key = True
                if len(x) == 0:
                    break
                chan.send(x)

    finally:
        # 重新设置终端属性
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, oldtty)

    
# thanks to Mike Looijmans for this code
def windows_shell(chan):
    import threading

    sys.stdout.write("Line-buffered terminal emulation. Press F6 or ^Z to send EOF.\r\n\r\n")
        
    def writeall(sock):
        while True:
            data = sock.recv(256)
            if not data:
                sys.stdout.write('\r\n*** EOF ***\r\n\r\n')
                sys.stdout.flush()
                break
            sys.stdout.write(data.decode())
            sys.stdout.flush()
        
    writer = threading.Thread(target=writeall, args=(chan,))
    writer.start()
        
    try:
        while True:
            d = sys.stdin.read(1)
            if not d:
                break
            chan.send(d)
    except EOFError:
        # user hit ^Z or F6
        pass
