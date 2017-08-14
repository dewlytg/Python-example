#coding:utf-8

###os模块
import os

os.sep              #取代操作系统特定的路径分隔符
os.linesep          #给出当前平台的行终止符。例如，Windows使用'\r\n'，Linux使用'\n'而Mac使用'\r'
os.name             #指示你正在使用的工作平台。比如对于Windows，它是'nt'，而对于Linux/Unix用户，它是'posix'。
os.getcwd()         #得到当前工作目录，即当前python脚本工作的目录路径。
os.curdir           #返回当前目录（'.'）
os.chdir()          #改变工作目录到dirname
os.listdir()        #返回指定目录下的所有文件和目录名
os.getenv()         #和os.putenv:分别用来读取和设置环境变量

os.stat()           #获得文件属性
os.chmod()          #修改文件权限和时间戳
os.remove()         #删除一个文件
os.mkdir()          #创建目录
os.rmdir()          #删除目录
os.removedirs()     #删除多个目录
os.system()         #运行shell命令

os.path.split()     #返回一个路径的目录名和文件名
os.path.isdir()     #判断name是不是目录，不是目录就返回false
os.path.isfile()    #判断name这个文件是否存在，不存在返回false
os.path.exists()    #判断是否存在文件或目录name
os.path.getsize()   #或得文件大小，如果name是目录返回0L
os.path.abspath()   #获得绝对路径
os.path.isabs()     #判断是否为绝对路径
os.path.normpath()  #规范path字符串形式
os.path.splitext()  #分离文件名和扩展名
os.path.join()      #连接目录与文件名或目录
os.path.basename()  #返回文件名
os.path.dirname()   #返回文件路径
os.path.getmtime()  #获取文件mtime值
os.path.getatime()  ##获取文件atime值
os.path.getctime()  ##获取文件ctime值
