#coding:utf-8

import optparse

# usage 定义的是使用方法，%prog 表示脚本本身，version定义的是脚本名字和版本号
parse = optparse.OptionParser(usage="usage:%prog [options] arg1,arg2",version="%prog 1.2")
parse.add_option('-u', '--user', dest='user', action='store', type=str, metavar='user', help='Enter User Name!!')
parse.add_option('-p', '--port', dest='port', type=int, metavar='port', default=3306, help='Enter Mysql Port!!')
parse.add_option('-v', help='Mysql Version!!')
# -u,--user 表示一个是短选项 一个是长选项
# dest='user' 将该用户输入的参数保存到变量user中，可以通过options.user方式来获取该值
# type=str，表示这个参数值的类型必须是str字符型，如果是其他类型那么将强制转换为str（可能会报错）
# metavar='user'，当用户查看帮助信息，如果metavar没有设值，那么显示的帮助信息的参数后面默认带上dest所定义的变量名
# help='Enter..',显示的帮助提示信息
# default=3306，表示如果参数后面没有跟值，那么将默认为变量default的值
parse.set_defaults(v=1.2)  # 也可以这样设置默认值
options, args = parse.parse_args()
print 'OPTIONS:', options
print 'ARGS:', args


print '~' * 20
print 'user:', options.user
print 'port:', options.port
print 'version:', options.v
print parse.format_help()