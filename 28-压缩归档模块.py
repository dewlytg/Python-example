#coding:utf-8

import zipfile

# 创建新的压缩文件
z = zipfile.ZipFile('docs.zip', 'w')
# 添加需要压缩的文件
z.write("c1.py")
z.write("c2.py")
z.close()

# 向已存在的压缩包中添加文件
z = zipfile.ZipFile('docs.zip', 'a')
# 添加需要压缩的文件
z.write("test.conf")
z.close()

# 解压缩所有文件
z = zipfile.ZipFile('docs.zip', 'r')
z.extractall()

# 解压缩指定文件

# 列出压缩包中的所有文件名
z = zipfile.ZipFile('docs.zip', 'r')
for i in z.namelist():
    print(i)

# 指定文件名称进行解压
z.extract("c1.py")
z.close()

########################################################################################
import tarfile

# 归档压缩
tf = tarfile.open('myprog.tar.gz', 'w:gz')
tf.add("MYPROG")
tf.close()

# 解压
tf = tarfile.open('myprog.tar.gz')
tf.extractall()
tf.close()

# 读取归档文件内容
tf = tarfile.open('myprog.tar.gz')
tf.list()
print(tf.getmembers())
f = tf.getmember('MYPROG/hello.py')
print(f.name)
print(f.size)
f.isfile()
tf.close()

##########################################################################################
import gzip

# 解压gzip文件示例:
f = gzip.open ('file.txt.gz', 'rb')
file_content = f.read ()
f.close ()

# 创建gzip文件:
content = "Lots of content here"
f = gzip.open('file.txt.gz', 'wb')
f.write(content)
f.close()

# gzip压缩现有文件:
f_in = open('file.txt', 'rb')
f_out = gzip.open ('file.txt.gz', 'wb')
f_out.writelines(f_in)
f_out.close()
f_in.close()