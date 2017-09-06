#coding:utf-8
"""
 Python执行系统命令的方法 os.system()，os.popen()，commands
"""
import os,commands

##os,无法获取输出和可以获取返回值
os.system("cat /proc/cpuinfo")

##os.popen,能获取输出无法获取返回值
output = os.popen("cat /proc/cpuinfo")
print output.read()

##commands,能获取输出和返回值
(status, output) = commands.getstatusoutput('cat /proc/cpuinfo')
print status, output
status,output = commands.getstatusoutput("ls /bin/ls")
print status,output
status,output = commands.getstatusoutput("cat /bin/tom")
print status,output
output = commands.getoutput("ls /bin/ls")
print output